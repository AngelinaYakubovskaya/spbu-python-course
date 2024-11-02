from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, BetType, Color
import random


class PercentageBot(BasePlayer):
    """Implements a betting strategy based on a percentage of the current balance."""

    def make_bet(self) -> Bet:
        """Makes a bet based on a percentage of the current balance."""
        amount = int(self.balance * 0.1)
        bet_type = random.choice(
            [BetType.COLOR, BetType.RANGE]
        )  # Используем BetType вместо строки

        # Устанавливаем значение ставки на основе типа ставки
        if bet_type == BetType.COLOR:
            bet_value = random.choice([Color.RED, Color.BLACK])
        elif bet_type == BetType.RANGE:
            bet_value = (1, 18)  # Для диапазона тип может быть tuple[int, int]
            return Bet(
                bet_type, bet_value, amount
            )  # Создаем Bet для диапазона отдельно

        # Создаем Bet для ставки по цвету
        return Bet(bet_type, bet_value, amount)
