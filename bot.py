# bot.py
import asyncio
import random
import json
import os
import math
from poke_env import LocalhostServerConfiguration
from poke_env.player import MaxBasePowerPlayer, Player

from config import BATTLE_FORMAT, SHOWDOWN_PASSWORD, SHOWDOWN_USERNAME, VGC_POLL_DATABASE

POLICY_FILE = "policy.json"


def generate_random_vgc_team():
  # Randomly pick 6 unique Pokémon sets from the pool to form a full VGC team
  chosen_mons = random.sample(VGC_POLL_DATABASE, 6)
  return "\n\n".join(chosen_mons)


class CustomTrainingBot(Player):

  def __init__(self, *args, learning_rate=0.05, epsilon=0.1, **kwargs):
    super().__init__(*args, **kwargs)
    # training bookkeeping
    self.training_score = 0
    self.recent_results = []

    # reinforcement learning policy: a simple table mapping action keys -> weight
    # action keys are strings like "move:thunderbolt" or "switch:charizard"
    self.policy = {}
    self.learning_rate = learning_rate
    self.epsilon = epsilon

    # per-battle action log to update policy after result is known
    self._current_battle_actions = []

    # try loading existing policy from disk so training can persist across runs
    self._load_policy()

  # --- Policy persistence ---
  def _load_policy(self):
    if os.path.exists(POLICY_FILE):
      try:
        with open(POLICY_FILE, "r") as f:
          data = json.load(f)
          # ensure numeric values
          self.policy = {k: float(v) for k, v in data.items()}
          print(f"[+] Loaded policy with {len(self.policy)} entries")
      except Exception as e:
        print(f"[!] Failed to load policy file: {e}")
        self.policy = {}

  def _save_policy(self):
    try:
      with open(POLICY_FILE, "w") as f:
        json.dump(self.policy, f)
    except Exception as e:
      print(f"[!] Failed to save policy file: {e}")

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
      base_score = base_power / 150.0
      weight = self._get_weight(move_key)
      combined = base_score + weight
      scores.append((m, combined))

    if random.random() < self.epsilon:
      chosen_move = random.choice(avail_moves)
    else:
      max_score = max(s for _, s in scores)
      exps = [math.exp(s - max_score) for _, s in scores]
      total = sum(exps)
      probs = [e / total for e in exps]
      r = random.random()
      cum = 0.0
      for (m, _), p in zip(scores, probs):
        cum += p
        if r <= cum:
          chosen_move = m
          break

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

      if battle.force_switch and battle.force_switch[i]:
        if battle.available_switches and battle.available_switches[i]:
          switch_choice = battle.available_switches[i][0]
          self._current_battle_actions.append(("switch", switch_choice.id))
          actions.append(switch_choice)
        else:
          actions.append(None)
        continue

      avail_moves = battle.available_moves[i] if battle.available_moves else []
      if avail_moves:
        chosen_move = self._select_move_from_candidates(avail_moves, battle, i)
        actions.append(chosen_move)
      else:
        if battle.available_switches and battle.available_switches[i]:
          switch_choice = battle.available_switches[i][0]
          self._current_battle_actions.append(("switch", switch_choice.id))
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

    reward = 1.0 if battle.won else -1.0
    for action_type, action_id in self._current_battle_actions:
      key = f"{action_type}:{action_id}"
      self._add_weight(key, self.learning_rate * reward)

    self.epsilon = max(0.01, self.epsilon * 0.995)
    self._save_policy()
    self._current_battle_actions = []


async def run_local_training():
  session_team = generate_random_vgc_team()

  baseline_bot = MaxBasePowerPlayer(
      battle_format=BATTLE_FORMAT,
      team=session_team,
      server_configuration=LocalhostServerConfiguration,
  )

  my_bot = CustomTrainingBot(
      battle_format=BATTLE_FORMAT,
      team=session_team,
      server_configuration=LocalhostServerConfiguration,
  )

  print(
      "[+] Starting local simulation training matches with a randomized 6-mon"
      " VGC team pool..."
  )
  await my_bot.battle_against(baseline_bot, n_battles=50)


if __name__ == "__main__":
  asyncio.run(run_local_training())
