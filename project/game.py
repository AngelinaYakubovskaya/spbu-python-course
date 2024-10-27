from typing import List
from project.bots.base_player import Player


class Game:
    """
    Class representing the roulette game.

    Attributes:
        players (List[Player]): List of players participating in the game.
        max_steps (int): The maximum number of steps (rounds) in the game.
        current_step (int): The current step (round) in the game.
    """

    def __init__(self, players: List[Player], max_steps: int = 10) -> None:
        """
        Initialize the game with players and a maximum number of steps.

        Args:
            players (List[Player]): List of players participating in the game.
            max_steps (int): The maximum number of steps in the game. Default is 10.
        """
        self.players = players
        self.max_steps = max_steps
        self.current_step = 0

    def run_game(self) -> None:
        """Run the game until completion or until the maximum steps are reached."""
        while not self.is_game_over():
            print(f"\n=== Round {self.current_step + 1} ===")
            self.play_round()
            self.show_game_state()
            self.current_step += 1
        print("\nGame Over!")
        self.show_winner()

    def is_game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over, otherwise False.
        """
        if self.current_step >= self.max_steps:
            return True
        active_players = [p for p in self.players if p.balance > 0]
        return len(active_players) <= 1

    def play_round(self) -> None:
        """Play a single round of the game."""
        for player in self.players:
            if player.balance > 0:
                bet, outcome = player.make_bet()
                win_amount = self.calculate_payout(bet, outcome)
                player.update_balance(win_amount - bet)

    def calculate_payout(self, bet: int, outcome: bool) -> int:
        """
        Calculate the payout based on the bet and the outcome.

        Args:
            bet (int): The amount bet by the player.
            outcome (bool): The outcome of the bet (True for win, False for loss).

        Returns:
            int: The payout amount.
        """
        return bet * 2 if outcome else 0

    def show_game_state(self) -> None:
        """Display the current state of the game."""
        for player in self.players:
            print(player)

    def show_winner(self) -> None:
        """Display the winner of the game, if any."""
        active_players = [p for p in self.players if p.balance > 0]
        if len(active_players) == 1:
            print(f"\n{active_players[0].name} wins the game!")
        else:
            print("\nThe game ended with no single winner.")
