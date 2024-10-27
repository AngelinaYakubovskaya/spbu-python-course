from project.bots.martingale_bot import MartingaleBot
from project.bots.percentage_bot import PercentageBot
from project.bots.passive_aggressive_bot import PassiveAggressiveBot


def test_martingale_bot_initialization():
    """Test the initialization of the Martingale bot."""
    bot = MartingaleBot("MartingaleBot")
    assert bot.name == "MartingaleBot"
    assert bot.balance == 100


def test_percentage_bot_initialization():
    """Test the initialization of the Percentage bot."""
    bot = PercentageBot("PercentageBot")
    assert bot.name == "PercentageBot"
    assert bot.balance == 100


def test_passive_aggressive_bot_initialization():
    """Test the initialization of the Passive Aggressive bot."""
    bot = PassiveAggressiveBot("PassiveAggressiveBot")
    assert bot.name == "PassiveAggressiveBot"
    assert bot.balance == 100
