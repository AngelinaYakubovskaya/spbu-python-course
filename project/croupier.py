import random
from project.bots.bet import Bet, BetType, Color


class Croupier:
    """
    Handles the outcome generation and bet evaluation in the roulette game.
    """

    def spin_wheel(self):
        number = random.randint(0, 36)
        color = Color.RED if number % 2 == 0 else Color.BLACK
        return {"number": number, "color": color}

    def check_bet(self, bet: Bet, result):
        """
        Checks if a bet matches the spin result.
        """
        if bet.bet_type == BetType.NUMBER and bet.value == result["number"]:
            return True
        elif bet.bet_type == BetType.COLOR and bet.value == result["color"]:
            return True
        elif bet.bet_type == BetType.RANGE:
            return bet.value[0] <= result["number"] <= bet.value[1]
        return False

    def payout_ratio(self, bet: Bet) -> int:
        """
        Определяет коэффициент выплат по выигрышной ставке.
        """
        if bet.bet_type == BetType.NUMBER:
            return 35
        elif bet.bet_type == BetType.COLOR:
            return 2
        elif bet.bet_type == BetType.RANGE:
            return 3
        return 0
