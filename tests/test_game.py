from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot
from project.game import Game
from project.croupier import Croupier
from project.bots.bet import BetType


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
    """Проверьте, правильно ли Croupier рассчитывает коэффициенты выплат в зависимости от типа ставки."""
    croupier = Croupier()

    # Создание ставок
    bet_number = Bet(bet_type=BetType.NUMBER, value=7, amount=10)
    bet_color = Bet(bet_type=BetType.COLOR, value=Color.RED, amount=10)
    bet_range = Bet(bet_type=BetType.RANGE, value=(1, 18), amount=10)

    # Проверка выплат для разных типов ставок
    assert croupier.payout_ratio(bet_number) == 35
    assert croupier.payout_ratio(bet_color) == 2
    assert croupier.payout_ratio(bet_range) == 3
