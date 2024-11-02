from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, BetType, Color  # Импортируем необходимые типы
import random


class PercentageBot(BasePlayer):
    """Implements a betting strategy based on a percentage of the current balance."""

    def make_bet(self) -> Bet:
        """Makes a bet based on a percentage of the current balance."""
        amount = int(self.balance * 0.1)
        bet_type = random.choice(
            [BetType.COLOR, BetType.RANGE]
        )  # Используем BetType вместо строки

        if bet_type == BetType.COLOR:
            bet_value = random.choice([Color.RED, Color.BLACK])
        else:
            bet_value = (1, 18)

        bet = Bet(bet_type, bet_value, amount)
        self.last_bet = bet
        return bet
