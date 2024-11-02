import pytest
from project.curry_uncarry import curry_explicit, uncurry_explicit


def test_curry_function():
    """Проверка каррированной функции."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    assert curried_add(3)(4) == 7  # Проверка, что каррирование работает корректно


def test_uncurry_function():
    """Проверка раскаррированной функции."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    uncurried_add = uncurry_explicit(curried_add, 2)
    assert uncurried_add(5, 7) == 12  # Проверка, что раскаррирование работает корректно


def test_frozen_arity():
    """Проверка зафиксированной арности и ошибки при дополнительных аргументах."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    curried_part = curried_add(1)  # Должно вернуть функцию
    assert callable(curried_part)

    # Проверка, что при попытке передать сразу два аргумента возникает ошибка
    with pytest.raises(TypeError):
        curried_add(1, 2)


def test_one_argument_per_call():
    """Проверка, что каррированная функция принимает только один аргумент за вызов."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        curried_add(1, 2)  # Ошибка, так как передается более одного аргумента


def test_zero_arity_function():
    """Тестирование каррирования и декаррирования для функции нулевой арности."""
    zero_arity_function = curry_explicit(lambda: "no args", 0)
    assert zero_arity_function() == "no args"  # Проверка вызова функции нулевой арности

    uncurried_zero_arity_function = uncurry_explicit(zero_arity_function, 0)
    assert (
        uncurried_zero_arity_function() == "no args"
    )  # Проверка раскаррирования нулевой арности
