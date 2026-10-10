# bot.py
import asyncio
import random
from poke_env import LocalhostServerConfiguration
from poke_env.player import MaxBasePowerPlayer, Player

from config import BATTLE_FORMAT, SHOWDOWN_PASSWORD, SHOWDOWN_USERNAME, VGC_POLL_DATABASE

def generate_random_vgc_team():
  # Randomly pick 6 unique Pokémon sets from the pool to form a full VGC team
  chosen_mons = random.sample(VGC_POLL_DATABASE, 6)
  return "\n\n".join(chosen_mons)


class CustomTrainingBot(Player):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.training_score = 0
    self.recent_results = []

  def choose_move(self, battle):
    if battle.in_team_preview:
      return self.choose_random_doubles_move(battle)

    actions = []
    for i, active_mon in enumerate(battle.active_pokemon):
      if not active_mon:
        actions.append(None)
        continue

      # Handle forced fainted switches
      if battle.force_switch and battle.force_switch[i]:
        if battle.available_switches and battle.available_switches[i]:
          actions.append(battle.available_switches[i][0])
        else:
          actions.append(None)
        continue

      avail_moves = battle.available_moves[i] if battle.available_moves else []
      if avail_moves:
        chosen_move = None
        move_ids = [m.id for m in avail_moves]

        # 1. Strategic utility priority
        if "trickroom" in move_ids and not battle.trick_room:
          chosen_move = next(m for m in avail_moves if m.id == "trickroom")
        elif "sleeppowder" in move_ids:
          chosen_move = next(m for m in avail_moves if m.id == "sleeppowder")
        elif "fakeout" in move_ids:
          chosen_move = next(m for m in avail_moves if m.id == "fakeout")
        # 2. Default to highest base power attack
        else:
          attacking_moves = [m for m in avail_moves if (m.base_power or 0) > 0]
          if attacking_moves:
            chosen_move = max(attacking_moves, key=lambda m: m.base_power)
          else:
            chosen_move = avail_moves[0]

        actions.append(chosen_move)
      else:
        if battle.available_switches and battle.available_switches[i]:
          actions.append(battle.available_switches[i][0])
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


async def run_local_training():
  # Generate a fresh random 6-mon VGC team for this training session
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