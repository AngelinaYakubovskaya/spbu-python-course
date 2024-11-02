from game import Game
from bots.martingale_bot import MartingaleBot
from bots.percentage_bot import PercentageBot
from bots.passive_aggressive_bot import PassiveAggressiveBot


def main():
    # Create instances of bots
    bot1 = MartingaleBot("MartingaleBot", 100)
    bot2 = PercentageBot("PercentageBot", 200, 0.1)  # Bet 10% of balance
    bot3 = PassiveAggressiveBot("PassiveAggressiveBot", 150)

    # Create the game
    game = Game(players=[bot1, bot2, bot3], max_steps=5)

    # Run the game
    game.run_game()


if __name__ == "__main__":
    main()
