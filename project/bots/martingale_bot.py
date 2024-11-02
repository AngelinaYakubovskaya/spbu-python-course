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


class MartingaleBot(BasePlayer):
    """
    Implements the Martingale betting strategy, doubling the bet on a loss.
    Attributes:
        base_bet (int): The initial bet amount.
        current_bet (int): The current bet amount that doubles after each loss.
    """

    def __init__(self, name: str, balance: int):
        """
        Initializes a MartingaleBot with a name and starting balance.
        Args:
            name (str): The name of the player.
            balance (int): The initial balance of the player.
        """
        super().__init__(name, balance)
        self.base_bet = 10
        self.current_bet = self.base_bet

    def make_bet(self) -> Bet:
        """
        Makes a bet according to the Martingale strategy.
        Returns:
            Bet: The bet made by the bot.
        """
        bet = Bet(BetType.COLOR, Color.RED.value, self.current_bet)
        self.last_bet = bet
        return bet

    def update_balance(self, amount: int):
        """
        Updates balance and adjusts the next bet amount based on the outcome.
        Args:
            amount (int): The win or loss amount from the previous bet.
        """
        super().update_balance(amount)
        if amount > 0:
            self.current_bet = self.base_bet
        else:
            self.current_bet *= 2
