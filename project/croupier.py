import random
from enum import Enum


class Color(Enum):
    RED = "red"
    BLACK = "black"
    GREEN = "green"  # Для нуля на рулетке


class Croupier:
    """
    Represents the croupier in the roulette game.
    """

    def __init__(self):
        self.last_result = None

    def spin_roulette(self):
        """
        Simulates spinning the roulette and returns the result.
        Returns:
            dict: The result containing 'number' and 'color'.
        """
        number = random.randint(0, 36)  # 0 to 36 for a standard roulette
        color = self.determine_color(number)
        self.last_result = {"number": number, "color": color}
        return self.last_result

    def determine_color(self, number: int) -> Color:
        """
        Determines the color based on the number.
        Args:
            number (int): The number on the roulette.
        Returns:
            Color: The color of the number.
        """
        if number == 0:
            return Color.GREEN
        elif number % 2 == 0:
            return Color.RED
        else:
            return Color.BLACK
