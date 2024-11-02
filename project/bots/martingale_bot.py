from project.bots.base_player import BasePlayer
from project.bots.bet import Bet, BetType, Color


class MartingaleBot(BasePlayer):
    """
    Implements the Martingale betting strategy, doubling the bet on a loss.
    """

    def __init__(self, name: str, balance: int):
        super().__init__(name, balance)
        self.base_bet = 10
        self.current_bet = self.base_bet

    def make_bet(self) -> Bet:
        bet = Bet(BetType.COLOR, Color.RED, self.current_bet)
        self.last_bet = bet
        return bet

    def update_balance(self, amount: int):
        super().update_balance(amount)
        if amount > 0:
            self.current_bet = self.base_bet
        else:
            self.current_bet *= 2
