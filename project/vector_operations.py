import math
from typing import Tuple, Optional


def scalar_product(len_a: float, len_b: float, angle: float) -> float:
    """Вычисляет скалярное произведение двух векторов."""
    return abs(len_a) * abs(len_b) * math.cos(math.radians(angle))


def length_vec(a: Optional[Tuple[float, float, float]], b: Optional[Tuple[float, float, float]]) -> float:
    """Вычисляет длину вектора между двумя точками a и b."""
    if a is None or b is None:
        raise ValueError("Одна из точек пуста или None")

    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)


def cos_ab(a: Optional[Tuple[float, float, float]], b: Optional[Tuple[float, float, float]]) -> float:
    """Вычисляет косинус угла между векторами a и b."""
    if a is None or b is None:
        raise ValueError("Один из векторов пуст или None")

    dot_product = (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
    magnitude_a = math.sqrt(a[0] ** 2 + a[1] ** 2 + a[2] ** 2)
    magnitude_b = math.sqrt(b[0] ** 2 + b[1] ** 2 + b[2] ** 2)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Длина одного из векторов равна нулю, невозможно вычислить косинус угла")

    return dot_product / (magnitude_a * magnitude_b)
