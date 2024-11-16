from enum import Enum


class BetType(Enum):
    COLOR = "color"
    NUMBER = "number"
    RANGE = "range"


class Color(Enum):
    RED = "red"
    BLACK = "black"


class Bet:
    def __init__(self, bet_type: BetType, value, amount: int):
        self.bet_type = bet_type
        self.value = value
        self.amount = amount

    def __repr__(self):
        return f"Bet(type={self.bet_type}, value={self.value}, amount={self.amount})"
