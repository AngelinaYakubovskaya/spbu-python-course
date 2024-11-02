from abc import ABC, abstractmethod


class BasePlayer(ABC):
    """
    Abstract base class for a player in the game.
    Attributes:
        name (str): The name of the player.
        balance (int): The current balance of the player.
    """

    def __init__(self, name: str, balance: int):
        """
        Initializes a BasePlayer with a name and starting balance.
        Args:
            name (str): The name of the player.
            balance (int): The initial balance of the player.
        """
        self.name = name
        self.balance = balance
        self.last_bet = None

    @abstractmethod
    def make_bet(self):
        """
        Abstract method for making a bet.
        Must be implemented by subclasses.
        """
        pass

    def update_balance(self, amount: int):
        """
        Updates the balance of the player.
        Args:
            amount (int): The amount to adjust the balance by (can be positive or negative).
        """
        self.balance += amount
