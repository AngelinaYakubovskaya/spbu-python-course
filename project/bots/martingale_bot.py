import random
from project.bots.base_player import Player


class MartingaleBot(Player):
    """
    A bot implementing the Martingale betting strategy.

    Attributes:
        last_bet (int): The last bet made by the bot.
        min_bet (int): The minimum bet amount.
    """

    def __init__(self, name: str, balance: int = 100) -> None:
        """
        Initialize a Martingale bot with a name and an initial balance.

        Args:
            name (str): The name of the bot.
            balance (int): The initial balance of the bot. Default is 100.
        """
        super().__init__(name, balance)
        self.min_bet = 10
        self.last_bet = self.min_bet

    def make_bet(self) -> tuple[int, bool]:
        """
        Make a bet using the Martingale strategy.

        Returns:
            tuple[int, bool]: The amount bet and whether the bet was successful.
        """
        bet = min(self.last_bet, self.balance)
        outcome = random.choice([True, False])
        print(f"{self.name} places a Martingale bet of {bet}")
        if outcome:
            self.last_bet = self.min_bet
        else:
            self.last_bet *= 2
        return bet, outcome
