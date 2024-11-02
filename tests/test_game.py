from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot
from project.game import Game
from project.croupier import Croupier


def test_game_initialization():
    """Test the initialization of the game."""
    players = [
        MartingaleBot("Bot1", 100),
        PercentageBot("Bot2", 100),
        PassiveAggressiveBot("Bot3", 100),
    ]
    game = Game(players=players, max_steps=10)
    assert len(game.players) == 3
    assert game.max_steps == 10
    assert game.current_step == 0


def test_game_state_changes():
    """Test that the game state changes after playing a round."""
    players = [
        MartingaleBot("Bot1", 100),
        PercentageBot("Bot2", 100),
        PassiveAggressiveBot("Bot3", 100),
    ]
    game = Game(players=players, max_steps=5)
    initial_balances = [player.balance for player in players]
    game.play_round()
    new_balances = [player.balance for player in players]
    assert initial_balances != new_balances


def test_croupier_payout():
    """Test if Croupier gives correct payout ratios based on bet type."""
    croupier = Croupier()
    # Проверка выплаты для разных типов ставок
    assert croupier.payout_ratio(BetType.NUMBER) == 35
    assert croupier.payout_ratio(BetType.COLOR) == 2
    assert croupier.payout_ratio(BetType.RANGE) == 3
