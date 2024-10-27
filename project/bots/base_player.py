class Player:
    """
    Base class for a player in the roulette game.

    Attributes:
        name (str): The name of the player.
        balance (int): The current balance of the player.
    """

    def __init__(self, name: str, balance: int = 100) -> None:
        """
        Initialize a player with a name and an initial balance.

        Args:
            name (str): The name of the player.
            balance (int): The initial balance of the player. Default is 100.
        """
        self.name = name
        self.balance = balance

    def make_bet(self) -> tuple[int, bool]:
        """
        Make a bet. This method should be overridden in derived classes.

        Raises:
            NotImplementedError: If the method is not implemented in a derived class.
        """
        raise NotImplementedError(
            "This method should be implemented in a bot strategy!"
        )

    def update_balance(self, amount: int) -> None:
        """
        Update the player's balance by adding the given amount.

        Args:
            amount (int): The amount to add to the player's balance.
        """
        self.balance += amount

    def __str__(self) -> str:
        """Return a string representation of the player."""
        return f"{self.name}: Balance = {self.balance}"
