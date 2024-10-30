import random


class Croupier:
    """
    Handles the outcome generation and bet evaluation in the roulette game.

    Methods:
        spin_wheel(): Generates a random outcome for a roulette spin.
        check_bet(bet, result): Checks if a player's bet matches the spin result.
        payout_ratio(bet): Returns the payout ratio based on the bet type.
    """

    def spin_wheel(self):
        """
        Spins the roulette wheel and returns the outcome.

        Returns:
            dict: A dictionary with the generated number (0-36) and color ("red" or "black").
        """
        number = random.randint(0, 36)
        color = "red" if number % 2 == 0 else "black"
        return {"number": number, "color": color}

    def check_bet(self, bet, result):
        """
        Checks if a bet matches the spin result.

        Args:
            bet (dict): The player's bet with 'type', 'value', and 'amount'.
            result (dict): The spin result with 'number' and 'color'.

        Returns:
            bool: True if the bet wins, False otherwise.
        """
        if bet["type"] == "number" and bet["value"] == result["number"]:
            return True
        elif bet["type"] == "color" and bet["value"] == result["color"]:
            return True
        elif bet["type"] == "range":
            return bet["value"][0] <= result["number"] <= bet["value"][1]
        return False

    def payout_ratio(self, bet):
        """
        Determines the payout ratio for a winning bet.

        Args:
            bet (dict): The player's bet.

        Returns:
            int: The payout ratio for the bet type.
        """
        if bet["type"] == "number":
            return 35
        elif bet["type"] == "color":
            return 2
        elif bet["type"] == "range":
            return 3
        return 1
