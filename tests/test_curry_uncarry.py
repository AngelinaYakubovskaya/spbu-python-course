import pytest
from project.curry_uncarry import curry_explicit, uncurry_explicit


def test_curry():
    f = curry_explicit(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    assert f(1)(2)(3) == "<1, 2, 3>"


def test_curry_zero_arity():
    f = curry_explicit(lambda: 6, 0)
    assert f() == 6


def test_curry_negative_arity():
    with pytest.raises(ValueError):
        curry_explicit(lambda x: x, -1)


def test_curry_single_arity():
    f = curry_explicit(lambda x: x, 1)
    assert f(36) == 36


def test_curry_built_in():
    f = curry_explicit(divmod, 2)
    assert f(5)(3) == (1, 2)


def test_curry_built_in_with_arbitrary_arity():
    f = curry_explicit(max, 3)

    # Проверка последовательного каррирования с каждым аргументом
    f1 = f(5)  # Первый этап каррирования, передаем первый аргумент
    f2 = f1(2)  # Второй этап каррирования, передаем второй аргумент
    f3 = f2(56)  # Третий этап каррирования, передаем третий аргумент

    # Проверяем результат после завершенного каррирования
    assert f3 == 56

    # Проверка, что каррированная функция вызывает TypeError при попытке передать более одного аргумента на этапе
    with pytest.raises(TypeError):
        f(1, 2)

    # Проверка, что каррированная функция вызывает TypeError при попытке передать более одного аргумента на последующих этапах
    with pytest.raises(TypeError):
        f1(2, 3)

    # Проверка, что вызов дополнительного аргумента после завершения каррирования вызывает TypeError
    with pytest.raises(TypeError):
        f3(4)  # Здесь `f3` уже должно быть результатом, а не функцией


def test_uncurry():
    f = curry_explicit(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    g = uncurry_explicit(f, 3)
    assert g(1, 2, 3) == "<1, 2, 3>"


def test_uncurry_incorrect_argument_count():
    f = curry_explicit(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    g = uncurry_explicit(f, 3)

    # Ensure too many arguments raise TypeError
    with pytest.raises(TypeError):
        g(1, 2, 3, 4)

    # Ensure too few arguments raise TypeError
    with pytest.raises(TypeError):
        g(1, 2)

    # Correct number of arguments should work
    assert g(1, 2, 3) == "<1, 2, 3>"


def test_uncurry_zero_arity():
    f = curry_explicit(lambda: 6, 0)
    g = uncurry_explicit(f, 0)
    assert g() == 6


def test_uncurry_negative_arity():
    with pytest.raises(ValueError):
        uncurry_explicit(lambda x: x, -1)


def test_uncurry_single_arity():
    f = curry_explicit(lambda x: x, 1)
    g = uncurry_explicit(f, 1)
    assert g(36) == 36


def test_uncurry_built_in():
    f = curry_explicit(divmod, 2)
    g = uncurry_explicit(f, 2)
    assert g(5, 3) == (1, 2)


def test_uncurry_built_in_with_arbitrary_arity():
    f = curry_explicit(max, 3)
    g = uncurry_explicit(f, 3)
    assert g(4, 7, 9) == 9

    # Ensure that only exactly three arguments are accepted
    with pytest.raises(TypeError):
        g(1, 2, 3, 9)
