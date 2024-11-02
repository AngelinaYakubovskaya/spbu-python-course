from project.bots.base_player import BasePlayer
from project.croupier import Croupier


class Game:
    """
    Represents the game of roulette.
    Attributes:
        players (List[BasePlayer]): The players participating in the game.
        max_steps (int): The maximum number of steps (rounds) to play.
        current_step (int): The current step (round) in the game.
        croupier (Croupier): The croupier managing the game.
    """

    def __init__(self, players: List[BasePlayer], max_steps: int):
        """
        Initializes a Game with players and maximum steps.
        Args:
            players (List[BasePlayer]): The players in the game.
            max_steps (int): The maximum number of steps to play.
        """
        self.players = players
        self.max_steps = max_steps
        self.current_step = 0
        self.croupier = Croupier()  # Initialize the croupier

    def play_round(self):
        """
        Plays a single round of the game.
        """
        # Spin the roulette to get the result
        result = self.croupier.spin_roulette()
        winning_color = result["color"]

        for player in self.players:
            bet = player.make_bet()
            if bet.bet_type == BetType.COLOR and bet.value == winning_color.value:
                # If the player's bet is a winning bet
                player.update_balance(
                    bet.amount
                )  # Here you might want to define the win amount
                print(f"{player.name} wins! Bet: {bet.amount} on {winning_color.value}")
            else:
                player.update_balance(-bet.amount)  # Player loses their bet

    def run_game(self):
        """
        Runs the game for the specified number of steps.
        """
        while self.current_step < self.max_steps:
            self.play_round()
            self.current_step += 1
