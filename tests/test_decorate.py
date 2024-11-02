import pytest
from project.decorate import (
    smart_args,
    Isolated,
    Evaluated,
    check_isolation,
    check_evaluation,
)


def test_check_isolation():
    """Тест для проверки работы изолированного аргумента Isolated."""
    no_mutable = {"a": 10}
    result = check_isolation(d=no_mutable)
    assert result == {"a": 0}  # Проверка, что возвращается измененный словарь {'a': 0}
    assert no_mutable == {"a": 10}  # Проверка, что исходный словарь не изменился


def test_check_evaluation():
    """Тест для проверки работы аргумента Evaluated."""
    result1 = check_evaluation()  # Первый вызов функции для проверки
    result2 = check_evaluation()  # Второй вызов функции для проверки
    assert result1[0] == result2[0]  # `x` должно оставаться постоянным между вызовами
    assert result1[1] != result2[1]  # `y` должно изменяться на каждом вызове

    result3 = check_evaluation(
        y=150
    )  # Задано значение для `y`, оно должно быть равно 150
    assert result3 == (result1[0], 150)
