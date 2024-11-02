from bots.base_player import BasePlayer
import random


class PassiveAggressiveBot(BasePlayer):
    """
    Implements a passive-aggressive betting strategy, randomly choosing between
    minimal and maximal bets.

    Methods:
        make_bet(): Bets either a small or a large amount randomly.
    """

    def make_bet(self):
        """
        Makes a bet by randomly choosing a minimal or large amount.

        Returns:
            dict: The bet with 'type', 'value', and 'amount'.
        """
        amount = 5 if random.choice([True, False]) else 50
        bet = {"type": "number", "value": random.randint(1, 36), "amount": amount}
        self.last_bet = bet
        return bet
