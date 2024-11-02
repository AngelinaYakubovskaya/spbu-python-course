from abc import ABC, abstractmethod
from project.bots.bet import Bet


class BasePlayer(ABC):
    """
    Abstract base class for a player in the roulette game.

    Attributes:
        name (str): The name of the player.
        balance (int): The player's current balance.
        last_bet (Bet): Stores the last bet made by the player.
    """

    def __init__(self, name: str, balance: int):
        """
        Initializes a player with a name and balance.

        Args:
            name (str): The name of the player.
            balance (int): The initial balance of the player.
        """
        self.name = name
        self.balance = balance
        self.last_bet: Bet = None  # Указываем, что last_bet будет экземпляром Bet

    @abstractmethod
    def make_bet(self) -> Bet:
        """
        Abstract method to be implemented by subclasses, specifying the player's betting strategy.

        Returns:
            Bet: The bet made by the player.
        """
        pass

    def update_balance(self, amount: int):
        """
        Updates the player's balance.

        Args:
            amount (int): The amount to add or subtract from the balance.
        """
        self.balance += amount

    def get_balance(self) -> int:
        """
        Returns the current balance of the player.

        Returns:
            int: The player's balance.
        """
        return self.balance
