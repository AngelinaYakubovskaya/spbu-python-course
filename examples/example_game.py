from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot
from project.game import Game


def run_example_game():
    """Run an example game of roulette and display the state in each round."""
    # Create players (bots) with initial balances
    bot1 = MartingaleBot("Martingale Bot", balance=100)
    bot2 = PercentageBot("Percentage Bot", balance=100)
    bot3 = PassiveAggressiveBot("Passive-Aggressive Bot", balance=100)

    # Initialize the game with the players
    game = Game(players=[bot1, bot2, bot3], max_steps=10)

    # Run the game
    print("Starting the Roulette Game!\n")
    game.run_game()

    # Display the final balances of players
    print("\nGame Over!")
    for player in game.players:
        print(f"{player.name} has a balance of {player.balance}")


if __name__ == "__main__":
    run_example_game()
