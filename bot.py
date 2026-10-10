import asyncio
from poke_env.player import Player
from poke_env.player.battle_order import DoubleBattleOrder
from poke_env import AccountConfiguration, ShowdownServerConfiguration
# Import configuration details from config.py
from config import BATTLE_FORMAT, SHOWDOWN_PASSWORD, SHOWDOWN_USERNAME, VGC_TEAM

class VGCMaxDamageBot(Player):
  def choose_move(self, battle):
    # Check if it's a double battle request
    if battle.in_team_preview:
      # Automatically select the first 4 Pokémon during team preview
      return self.choose_random_doubles_move(battle)

    # For standard turns in VGC, we need orders for both active Pokémon slots
    if battle.active_pokemon:
      orders = []
      for pokemon in battle.active_pokemon:
        # Find the available moves for this specific active Pokémon
        available_moves = [
            m for m in battle.available_moves if m.gen_pai_is_valid_target
        ]  # or check pokemon.moves

      # Fallback to random doubles choice if custom logic gets complex
      return self.choose_random_doubles_move(battle)

    return self.choose_random_doubles_move(battle)

# Alternative simpler built-in baseline bot for VGC:
# poke-env includes built-in random and heuristic templates that natively handle doubles.
from poke_env.player.baselines import MaxBasePowerPlayer

class VGCHeuristicBot(MaxBasePowerPlayer):
  pass
  account_config = AccountConfiguration(SHOWDOWN_USERNAME, SHOWDOWN_PASSWORD)

async def main():
  # Configure your bot credentials (use guest mode or real account info)
  # For local testing, you can pit two Python bots against each other:
  player_1 = VGCHeuristicBot(
      battle_format=BATTLE_FORMAT,
      team=VGC_TEAM,
      server_configuration=ShowdownServerConfiguration,
  )

  player_2 = VGCHeuristicBot(battle_format=BATTLE_FORMAT)

  print("[+] Starting test battle between two Python VGC bots...")
  await player_1.battle_against(player_2, n_battles=1)
  print(f"[+] Battle finished! Won: {player_1.n_won_battles}")

class VGCHeuristicBot(MaxBasePowerPlayer):
  pass

async def run_bot():
  bot = VGCHeuristicBot(
      account_configuration=account_config,
      server_configuration=ShowdownServerConfiguration,
      battle_format=BATTLE_FORMAT,
      team=VGC_TEAM,
      # Set max_concurrent_battles to accept multiple challenges at once
      max_concurrent_battles=3,
  )

  print("[+] Bot is online and listening for VGC challenges...")
  # Play a specific number of games on the official ladder (e.g., 10 games)
  await bot.ladder(10)

if __name__ == "__main__":
  asyncio.run(run_bot())