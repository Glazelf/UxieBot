# bot.py
import asyncio
import random
import json
import os
import math
from poke_env import LocalhostServerConfiguration
from poke_env.player import MaxBasePowerPlayer, Player

from config import BATTLE_FORMAT, SHOWDOWN_PASSWORD, SHOWDOWN_USERNAME, VGC_POLL_DATABASE

DEFAULT_POLICY_FILE = "policy.json"


def generate_random_vgc_team():
  # Randomly pick 6 unique Pokémon sets from the pool to form a full VGC team
  chosen_mons = random.sample(VGC_POLL_DATABASE, 6)
  return "\n\n".join(chosen_mons)


class CustomTrainingBot(Player):

  def __init__(self, *args, policy_file: str = DEFAULT_POLICY_FILE, learning_rate=0.05, epsilon=0.1, **kwargs):
    super().__init__(*args, **kwargs)
    # training bookkeeping
    self.training_score = 0
    self.recent_results = []

    # reinforcement learning policy: a simple table mapping action keys -> weight
    # action keys are strings like "move:thunderbolt" or "switch:charizard"
    self.policy = {}
    self.learning_rate = learning_rate
    self.epsilon = epsilon

    # where to persist this bot's policy (so two bots can have independent policies)
    self.policy_file = policy_file

    # per-battle action log to update policy after result is known
    self._current_battle_actions = []

    # try loading existing policy from disk so training can persist across runs
    self._load_policy()

  # --- Policy persistence ---
  def _load_policy(self):
    if os.path.exists(self.policy_file):
      try:
        with open(self.policy_file, "r") as f:
          data = json.load(f)
          # ensure numeric values
          self.policy = {k: float(v) for k, v in data.items()}
          print(f"[+] Loaded policy ({self.policy_file}) with {len(self.policy)} entries")
      except Exception as e:
        print(f"[!] Failed to load policy file {self.policy_file}: {e}")
        self.policy = {}

  def _save_policy(self):
    try:
      with open(self.policy_file, "w") as f:
        json.dump(self.policy, f)
    except Exception as e:
      print(f"[!] Failed to save policy file {self.policy_file}: {e}")

  # --- Helper for policy values ---
  def _get_weight(self, action_key):
    return self.policy.get(action_key, 0.0)

  def _add_weight(self, action_key, delta):
    self.policy[action_key] = self._get_weight(action_key) + delta

  # --- Action selection using a simple softmax/epsilon-greedy hybrid ---
  def _select_move_from_candidates(self, avail_moves, battle, side_index):
    scores = []
    for m in avail_moves:
      move_key = f"move:{m.id}"
      base_power = m.base_power or 0
      # Normalize base power (simple): divide by 150 to keep same order
      base_score = base_power / 150.0
      weight = self._get_weight(move_key)
      combined = base_score + weight

      # Penalize pure-status moves slightly to avoid Protect/Status spam early in training
      # Many status moves have base_power == 0; this small penalty encourages damaging moves
      if base_power == 0:
        combined -= 0.12

      scores.append((m, combined))

    # Epsilon-greedy: with prob epsilon, choose a random move to explore
    if random.random() < self.epsilon:
      chosen_move = random.choice(avail_moves)
    else:
      # softmax sampling to maintain stochasticity while biasing towards higher scores
      max_score = max(s for _, s in scores)
      exps = [math.exp(s - max_score) for _, s in scores]
      total = sum(exps)
      probs = [e / total for e in exps]
      r = random.random()
      cum = 0.0
      chosen_move = avail_moves[0]
      for (m, _), p in zip(scores, probs):
        cum += p
        if r <= cum:
          chosen_move = m
          break

    # log action for learning
    self._current_battle_actions.append(("move", chosen_move.id))
    return chosen_move

  def choose_move(self, battle):
    if battle.in_team_preview:
      return self.choose_random_doubles_move(battle)

    actions = []
    for i, active_mon in enumerate(battle.active_pokemon):
      if not active_mon:
        actions.append(None)
        continue

      # Handle forced fainted switches
      if getattr(battle, "force_switch", None) and battle.force_switch[i]:
        if getattr(battle, "available_switches", None) and battle.available_switches[i]:
          switch_choice = battle.available_switches[i][0]
          # Pokemon objects from poke_env don't have an `id` attribute. Use species/name
          switch_id = getattr(switch_choice, "species", None) or getattr(switch_choice, "name", None) or str(switch_choice)
          self._current_battle_actions.append(("switch", switch_id))
          actions.append(switch_choice)
        else:
          actions.append(None)
        continue

      avail_moves = battle.available_moves[i] if getattr(battle, "available_moves", None) else []
      if avail_moves:
        chosen_move = self._select_move_from_candidates(avail_moves, battle, i)
        actions.append(chosen_move)
      else:
        if getattr(battle, "available_switches", None) and battle.available_switches[i]:
          switch_choice = battle.available_switches[i][0]
          switch_id = getattr(switch_choice, "species", None) or getattr(switch_choice, "name", None) or str(switch_choice)
          self._current_battle_actions.append(("switch", switch_id))
          actions.append(switch_choice)
        else:
          actions.append(None)

    valid_actions = [a for a in actions if a is not None]

    if len(valid_actions) >= 2:
      return self.create_order(valid_actions[0], valid_actions[1])
    elif len(valid_actions) == 1:
      return self.create_order(valid_actions[0])

    return self.choose_random_doubles_move(battle)

  def _battle_finished(self, battle):
    result = 1 if battle.won else 0
    self.recent_results.append(result)
    if len(self.recent_results) > 20:
      self.recent_results.pop(0)

    rolling_win_rate = (
        sum(self.recent_results) / len(self.recent_results)
    ) * 100

    if battle.won:
      self.training_score += 10
      print(
          f"[+] Match WON against {battle.opponent_username}! Score:"
          f" {self.training_score} | Rolling Win Rate (Last"
          f" {len(self.recent_results)}): {rolling_win_rate:.1f}%"
      )
    else:
      self.training_score -= 10
      print(
          f"[-] Match LOST against {battle.opponent_username}. Score:"
          f" {self.training_score} | Rolling Win Rate (Last"
          f" {len(self.recent_results)}): {rolling_win_rate:.1f}%"
      )

    # Convert battle outcome to a reward: +1 for win, -1 for loss
    reward = 1.0 if battle.won else -1.0

    # Update policy weights based on actions taken during this battle
    # Simple update: for each action_key, add lr * reward
    for action_type, action_id in self._current_battle_actions:
      key = f"{action_type}:{action_id}"
      self._add_weight(key, self.learning_rate * reward)

    # Decay epsilon slightly so we explore less over time
    self.epsilon = max(0.01, self.epsilon * 0.995)

    # Save the updated policy to disk
    self._save_policy()

    # Clear current battle actions for next battle
    self._current_battle_actions = []


async def run_local_training():
  # Generate a fresh random 6-mon VGC team for this training session
  session_team = generate_random_vgc_team()

  # Create two RL-enabled bots with separate policy files so they can both learn
  baseline_bot = CustomTrainingBot(
      battle_format=BATTLE_FORMAT,
      team=session_team,
      server_configuration=LocalhostServerConfiguration,
      policy_file="policy_baseline.json",
      learning_rate=0.02,
      epsilon=0.2,
  )

  my_bot = CustomTrainingBot(
      battle_format=BATTLE_FORMAT,
      team=session_team,
      server_configuration=LocalhostServerConfiguration,
      policy_file="policy_mine.json",
      learning_rate=0.05,
      epsilon=0.1,
  )

  print(
      "[+] Starting local simulation training matches with a randomized 6-mon"
      " VGC team pool..."
  )
  # Battle both RL bots against each other
  await my_bot.battle_against(baseline_bot, n_battles=50)


if __name__ == "__main__":
  asyncio.run(run_local_training())
