import math
from typing import Tuple


def scalar_product(len_a: float, len_b: float, angle: float) -> float:
    """Возвращает скалярное произведение векторов через длины и угол между ними."""
    return abs(len_a) * abs(len_b) * math.cos(math.radians(angle))


def length_vec(A: Tuple[float, float, float], B: Tuple[float, float, float]) -> float:
    """Вычисляет длину вектора между двумя точками A и B."""
    return math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2 + (B[2] - A[2]) ** 2)


def cos_AB(A: Tuple[float, float, float], B: Tuple[float, float, float]) -> float:
    """Вычисляет косинус угла между векторами A и B."""
    dot_product = (A[0] * B[0]) + (A[1] * B[1]) + (A[2] * B[2])
    magnitude_A = math.sqrt(A[0] ** 2 + A[1] ** 2 + A[2] ** 2)
    magnitude_B = math.sqrt(B[0] ** 2 + B[1] ** 2 + B[2] ** 2)

    if magnitude_A == 0 or magnitude_B == 0:
        raise ValueError(
            "Длина одного из векторов равна нулю, невозможно вычислить косинус угла"
        )

    return dot_product / (magnitude_A * magnitude_B)