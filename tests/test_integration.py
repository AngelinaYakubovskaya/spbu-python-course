from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot
from project.game import Game


def test_full_game_run():
    """Test the full game run and check if the game ends correctly."""
    players = [
        MartingaleBot("Bot1", 100),
        PercentageBot("Bot2", 100),
        PassiveAggressiveBot("Bot3", 100),
    ]
    game = Game(players=players, max_steps=5)
    game.run_game()
    winners = [p for p in game.players if p.balance > 0]
    assert len(winners) >= 1 or game.current_step == game.max_steps
