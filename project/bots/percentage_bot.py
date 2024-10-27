import random
from project.bots.base_player import Player


class PercentageBot(Player):
    """
    A bot implementing a percentage-based betting strategy.

    Attributes:
        percentage (float): The percentage of the balance to bet.
    """

    def __init__(self, name: str, balance: int = 100) -> None:
        """
        Initialize a percentage bot with a name and an initial balance.

        Args:
            name (str): The name of the bot.
            balance (int): The initial balance of the bot. Default is 100.
        """
        super().__init__(name, balance)
        self.percentage = 0.1

    def make_bet(self) -> tuple[int, bool]:
        """
        Make a bet based on a percentage of the balance.

        Returns:
            tuple[int, bool]: The amount bet and whether the bet was successful.
        """
        bet = max(1, int(self.balance * self.percentage))
        outcome = random.choice([True, False])
        print(f"{self.name} places a percentage bet of {bet}")
        return bet, outcome
