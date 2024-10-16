import pytest
from project.rgba import rgba_vector


@pytest.mark.parametrize(
    "index, expected_rgba",
    [
        (1, (0, 0, 0, 0)),  # Первый RGBA элемент
        (2, (0, 0, 0, 2)),  # Второй RGBA элемент
        (3, (0, 0, 0, 4)),  # Третий RGBA элемент
        (1000000, (15, 151, 151, 100)),  # Большой индекс, ожидаемое значение
        (16581375, (255, 255, 255, 100)),  # Последний валидный RGBA элемент
    ],
)
def test_rgba_vector(index, expected_rgba):
    """Тест генератора RGBA векторов для различных индексов."""
    assert rgba_vector(index) == expected_rgba


def test_rgba_out_of_range():
    """Тест генератора RGBA для индекса вне диапазона."""
    assert rgba_vector(16581376) is None  # Индекс вне границ возвращает None


def test_invalid_input():
    """Тест генератора RGBA для недопустимого ввода."""
    assert rgba_vector("a") is None  # Неправильный тип (строка)
    assert rgba_vector(-1) is None  # Отрицательный индекс
    assert rgba_vector(0) is None  # Индекс не может быть нулем
    assert rgba_vector(16581376) is None  # Индекс превышает максимальный
