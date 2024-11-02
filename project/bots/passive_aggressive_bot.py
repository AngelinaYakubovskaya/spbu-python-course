from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, BetType
import random


class PassiveAggressiveBot(BasePlayer):
    """
    Implements a passive-aggressive betting strategy, randomly choosing between
    minimal and maximal bets.
    """

    def make_bet(self) -> Bet:
        amount = 5 if random.choice([True, False]) else 50
        bet = Bet(BetType.NUMBER, random.randint(1, 36), amount)
        self.last_bet = bet
        return bet
