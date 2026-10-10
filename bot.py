import asyncio
from poke_env.player import Player
from poke_env.player.battle_order import DoubleBattleOrder
from poke_env import AccountConfiguration, ShowdownServerConfiguration
import asyncio

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

async def main():
  # Configure your bot credentials (use guest mode or real account info)
  # For local testing, you can pit two Python bots against each other:
  player_1 = VGCHeuristicBot(
      battle_format="gen9championsvgc2026regmc",
      team=VGC_TEAM,
      server_configuration=ShowdownServerConfiguration,
  )

  player_2 = VGCHeuristicBot(battle_format="gen9championsvgc2026regmc")

  print("[+] Starting test battle between two Python VGC bots...")
  await player_1.battle_against(player_2, n_battles=1)
  print(f"[+] Battle finished! Won: {player_1.n_won_battles}")

class VGCHeuristicBot(MaxBasePowerPlayer):
  pass

# Optional: Set a specific username and password (or leave blank for guest)
config = AccountConfiguration("UxieIsCool", "appelsap")

# Standard VGC Team in Showdown Export format
VGC_TEAM = """
Indeedee (M) @ Focus Sash  
Ability: Psychic Surge  
Level: 50  
EVs: 2 HP / 32 SpA / 32 Spe  
Timid Nature  
- Protect  
- Expanding Force  
- Imprison  
- Trick Room  

Gliscor @ Psychic Seed  
Ability: Hyper Cutter  
Level: 50  
EVs: 15 HP / 25 Atk / 26 Spe  
Adamant Nature  
- Protect  
- High Horsepower  
- Acrobatics  
- Tailwind  

Kingambit @ Chople Berry  
Ability: Defiant  
Level: 50  
EVs: 32 HP / 9 Atk / 14 Def / 11 SpD  
Adamant Nature  
- Kowtow Cleave  
- Iron Head  
- Sucker Punch  
- Low Kick  

Charizard @ Charizardite Y  
Ability: Blaze  
Level: 50  
EVs: 32 HP / 11 Def / 1 SpA / 21 SpD / 1 Spe  
Modest Nature  
- Protect  
- Heat Wave  
- Ancient Power  
- Weather Ball  

Annihilape @ Choice Scarf  
Ability: Defiant  
Level: 50  
EVs: 32 Atk / 2 Def / 32 Spe  
Jolly Nature  
- Close Combat  
- Phantom Force  
- Ice Punch  
- Rock Slide  

Venusaur @ Wide Lens  
Ability: Chlorophyll  
Level: 50  
EVs: 24 HP / 12 SpA / 30 Spe  
Timid Nature  
- Protect  
- Sludge Bomb  
- Leaf Storm  
- Sleep Powder  
""".strip()

async def run_bot():
  bot = VGCHeuristicBot(
      account_configuration=config,
      server_configuration=ShowdownServerConfiguration,
      battle_format="gen9championsvgc2026regmc",
      team=VGC_TEAM,
      # Set max_concurrent_battles to accept multiple challenges at once
      max_concurrent_battles=3,
  )

  print("[+] Bot is online and listening for VGC challenges...")
  # Play a specific number of games on the official ladder (e.g., 10 games)
  await bot.ladder(10)

if __name__ == "__main__":
  asyncio.run(run_bot())