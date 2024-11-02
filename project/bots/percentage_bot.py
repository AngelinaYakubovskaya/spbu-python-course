from enum import Enum
from project.bots.base_player import BasePlayer


class BetType(Enum):
    COLOR = "color"
    NUMBER = "number"


class Color(Enum):
    RED = "red"
    BLACK = "black"


class Bet:
    """
    Represents a bet made by a player.
    Attributes:
        bet_type (BetType): The type of the bet (e.g., color, number).
        value (str or int): The value of the bet (e.g., "red" or a specific number).
        amount (int): The amount being bet.
    """

    def __init__(self, bet_type: BetType, value, amount: int):
        self.bet_type = bet_type
        self.value = value
        self.amount = amount


class PercentageBot(BasePlayer):
    """
    Implements a betting strategy based on a fixed percentage of the balance.
    """

    def __init__(self, name: str, balance: int):
        """
        Initializes a PercentageBot with a name and starting balance.
        Args:
            name (str): The name of the player.
            balance (int): The initial balance of the player.
        """
        super().__init__(name, balance)

    def make_bet(self) -> Bet:
        """
        Makes a bet based on a percentage of the current balance.
        Returns:
            Bet: The bet made by the bot.
        """
        bet_amount = int(self.balance * 0.1)  # Betting 10% of balance
        bet = Bet(BetType.COLOR, Color.RED.value, bet_amount)
        self.last_bet = bet
        return bet
