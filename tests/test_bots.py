from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot
from project.bots.bet import BetType  # Импортируем BetType для проверок ставок


def test_martingale_bot_initialization():
    """Test the initialization of the Martingale bot."""
    bot = MartingaleBot("MartingaleBot", 100)
    assert bot.name == "MartingaleBot"
    assert bot.balance == 100


def test_martingale_bot_make_bet():
    """Test if Martingale bot makes a valid Bet."""
    bot = MartingaleBot("MartingaleBot", 100)
    bet = bot.make_bet()
    assert bet.bet_type == BetType.COLOR
    assert bet.value == "red"
    assert bet.amount > 0


def test_percentage_bot_initialization():
    """Test the initialization of the Percentage bot."""
    bot = PercentageBot("PercentageBot", 100)
    assert bot.name == "PercentageBot"
    assert bot.balance == 100


def test_percentage_bot_make_bet():
    """Test if Percentage bot makes a valid Bet."""
    bot = PercentageBot("PercentageBot", 100)
    bet = bot.make_bet()
    assert bet.amount == int(
        bot.balance * 0.1
    )  # Проверяем, что ставка – 10% от баланса
    assert bet.bet_type in [BetType.COLOR, BetType.RANGE]


def test_passive_aggressive_bot_initialization():
    """Test the initialization of the Passive Aggressive bot."""
    bot = PassiveAggressiveBot("PassiveAggressiveBot", 100)
    assert bot.name == "PassiveAggressiveBot"
    assert bot.balance == 100


def test_passive_aggressive_bot_make_bet():
    """Test if Passive Aggressive bot makes a valid Bet."""
    bot = PassiveAggressiveBot("PassiveAggressiveBot", 100)
    bet = bot.make_bet()
    assert bet.bet_type == BetType.NUMBER
    assert (
        1 <= bet.value <= 36
    )  # Проверяем, что номер находится в пределах возможного диапазона
    assert bet.amount in [5, 50]
