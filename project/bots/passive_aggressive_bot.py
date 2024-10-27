import random
from project.bots.base_player import Player


class PassiveAggressiveBot(Player):
    """
    A bot that alternates between aggressive and passive betting.

    Attributes:
        aggressive (bool): Indicates if the next bet will be aggressive.
    """

    def __init__(self, name: str, balance: int = 100) -> None:
        """
        Initialize a passive-aggressive bot with a name and an initial balance.

        Args:
            name (str): The name of the bot.
            balance (int): The initial balance of the bot. Default is 100.
        """
        super().__init__(name, balance)
        self.aggressive = False

    def make_bet(self) -> tuple[int, bool]:
        """
        Make a bet that alternates between high and low amounts.

        Returns:
            tuple[int, bool]: The amount bet and whether the bet was successful.
        """
        bet = min(20 if self.aggressive else 5, self.balance)
        outcome = random.choice([True, False])
        print(
            f"{self.name} places a {'high' if self.aggressive else 'low'} bet of {bet}"
        )
        self.aggressive = not self.aggressive
        return bet, outcome
