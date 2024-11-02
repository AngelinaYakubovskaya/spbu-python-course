from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, BetType, Color
import random


class PercentageBot(BasePlayer):
    """Implements a betting strategy based on a percentage of the current balance."""

    def make_bet(self) -> Bet:
        """Makes a bet based on a percentage of the current balance."""
        amount = int(self.balance * 0.1)
        bet_type = random.choice([BetType.COLOR, BetType.RANGE])

        if bet_type == BetType.COLOR:
            bet_value = random.choice([Color.RED, Color.BLACK])
            return Bet(bet_type, bet_value, amount)

        elif bet_type == BetType.RANGE:
            range_value = (1, 18)
            return Bet(bet_type, range_value, amount)

        # Добавляем assert, чтобы указать, что ни один другой случай невозможен
        assert False, "Unhandled BetType in make_bet"
