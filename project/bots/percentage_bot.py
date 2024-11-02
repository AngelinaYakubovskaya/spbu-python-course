from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, BetType
import random


class PercentageBot(BasePlayer):
    """
    Implements a betting strategy based on a percentage of the current balance.
    """

    def make_bet(self) -> Bet:
        amount = int(self.balance * 0.1)
        bet_type = random.choice([BetType.COLOR, BetType.RANGE])
        if bet_type == BetType.COLOR:
            bet_value = Color.RED
        else:
            bet_value = (1, 18)  # Example range
        bet = Bet(bet_type, bet_value, amount)
        self.last_bet = bet
        return bet
