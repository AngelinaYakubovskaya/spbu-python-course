from project.bots.base_player import BasePlayer
from project.croupier import Croupier
from typing import List


class Game:
    """
    Manages the main game loop and interactions between players and the croupier.
    """

    def __init__(self, players: List[BasePlayer], max_steps: int):
        self.players = players
        self.croupier = Croupier()
        self.max_steps = max_steps
        self.current_step = 0

    def play_round(self):
        bets = {player: player.make_bet() for player in self.players}
        result = self.croupier.spin_wheel()

        for player, bet in bets.items():
            if self.croupier.check_bet(bet, result):
                player.update_balance(bet.amount * self.croupier.payout_ratio(bet))
            else:
                player.update_balance(-bet.amount)

    def run_game(self):
        for _ in range(self.max_steps):
            self.play_round()
            self.current_step += 1
            if all(player.balance <= 0 for player in self.players):
                break

    def get_game_state(self):
        return {
            "round": self.current_step,
            "players": {player.name: player.balance for player in self.players},
        }
