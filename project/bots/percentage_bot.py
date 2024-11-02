from project.bots.base_player import BasePlayer
import random


class PercentageBot(BasePlayer):
    """
    Implements a betting strategy based on a percentage of the current balance.

    Methods:
        make_bet(): Bets a portion of the current balance on a random field.
    """

    def make_bet(self):
        """
        Makes a bet based on a percentage of the current balance.

        Returns:
            dict: The bet with 'type', 'value', and 'amount'.
        """
        amount = int(self.balance * 0.1)
        bet_type = random.choice(["color", "range"])
        bet_value = "red" if bet_type == "color" else (1, 18)
        bet = {"type": bet_type, "value": bet_value, "amount": amount}
        self.last_bet = bet
        return bet
