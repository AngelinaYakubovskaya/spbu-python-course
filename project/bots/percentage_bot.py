from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, Color
import random


class PercentageBot(BasePlayer):
    """Implements a betting strategy based on a percentage of the current balance."""

    def make_bet(self) -> Bet:
        """Makes a bet based on a percentage of the current balance."""
        amount = int(self.balance * 0.1)
        bet_type = random.choice(["color", "range"])
        bet_value = Color.RED if bet_type == "color" else (1, 18)
        bet = Bet(bet_type, bet_value, amount)
        self.last_bet = bet
        return bet
