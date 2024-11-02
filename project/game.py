from bots.base_player import BasePlayer
from croupier import Croupier
from typing import List


class Game:
    """
    Manages the main game loop and interactions between players and the croupier.

    Attributes:
        players (List[BasePlayer]): List of player instances participating in the game.
        croupier (Croupier): Instance of Croupier handling outcomes and bet validations.
        max_steps (int): Maximum number of rounds the game will run.
        current_step (int): Counter for the current game round.
    """

    def __init__(self, players: List[BasePlayer], max_steps: int):
        """
        Initializes the Game with a list of players and a maximum number of steps.

        Args:
            players (List[BasePlayer]): List of players participating in the game.
            max_steps (int): The maximum number of rounds for the game.
        """
        self.players = players
        self.croupier = Croupier()
        self.max_steps = max_steps
        self.current_step = 0

    def play_round(self):
        """
        Executes a single round of betting for all players, evaluates results through
        the Croupier, and updates player balances accordingly.
        """
        bets = {player: player.make_bet() for player in self.players}
        result = self.croupier.spin_wheel()

        for player, bet in bets.items():
            if self.croupier.check_bet(bet, result):
                player.update_balance(bet["amount"] * self.croupier.payout_ratio(bet))
            else:
                player.update_balance(-bet["amount"])

    def run_game(self):
        """
        Runs the game until either all players lose their balance or the maximum
        number of steps is reached.
        """
        for _ in range(self.max_steps):
            self.play_round()
            self.current_step += 1
            if all(player.balance <= 0 for player in self.players):
                break

    def get_game_state(self):
        """
        Provides the current state of the game, including the round number and player balances.

        Returns:
            dict: A dictionary containing the current round and the balance of each player.
        """
        return {
            "round": self.current_step,
            "players": {player.name: player.balance for player in self.players},
        }
