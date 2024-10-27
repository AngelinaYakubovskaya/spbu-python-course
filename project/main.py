from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot
from project.game import Game

if __name__ == "__main__":
    bot1 = MartingaleBot("Martingale Bot")
    bot2 = PercentageBot("Percentage Bot")
    bot3 = PassiveAggressiveBot("Passive-Aggressive Bot")

    game = Game(players=[bot1, bot2, bot3], max_steps=10)
    game.run_game()
