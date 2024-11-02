import pytest
from project.curry_uncurry import explicit_curry, explicit_uncurry

# Tests for explicit_curry
@pytest.mark.parametrize(
    "args, expected",
    [
        ((1, 2, 3), "<1, 2, 3>"),
        ((10, 20, 30), "<10, 20, 30>"),
        ((5, 5, 5), "<5, 5, 5>"),
    ],
)
def test_curry_explicit_valid_cases(args, expected):
    curried_func = explicit_curry(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    assert curried_func(*args) == expected


def test_curry_explicit_arity_zero():
    curried_func = explicit_curry(lambda: "No args", 0)
    assert curried_func() == "No args"


def test_curry_explicit_arity_one():
    curried_func = explicit_curry(lambda x: x * 2, 1)
    assert curried_func(5) == 10


@pytest.mark.parametrize("args", [(1, 2, 3), (1, 2, 3, 4)])
def test_curry_explicit_too_many_arguments(args):
    curried_func = explicit_curry(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        curried_func(*args)


@pytest.mark.parametrize("arity", [-1, "a"])
def test_curry_explicit_invalid_arity(arity):
    with pytest.raises(ValueError):
        explicit_curry(lambda x: x, arity)


def test_curry_explicit_function_with_arbitrary_args():
    curried_func = explicit_curry(print, 2)
    assert curried_func(1)(2) is None


# Tests for explicit_uncurry
@pytest.mark.parametrize(
    "args, expected",
    [
        ((1, 2, 3), "<1, 2, 3>"),
        ((4, 5, 6), "<4, 5, 6>"),
    ],
)
def test_uncurry_explicit_valid_cases(args, expected):
    curried_func = explicit_curry(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    uncurried_func = explicit_uncurry(curried_func, 3)
    assert uncurried_func(*args) == expected


@pytest.mark.parametrize("args", [(1,), (1, 2, 3)])
def test_uncurry_explicit_wrong_argument_count(args):
    curried_func = explicit_curry(lambda x, y: x + y, 2)
    uncurried_func = explicit_uncurry(curried_func, 2)
    with pytest.raises(TypeError):
        uncurried_func(*args)


@pytest.mark.parametrize("arity", [-1, "a"])
def test_uncurry_explicit_invalid_arity(arity):
    curried_func = explicit_curry(lambda x: x, 1)
    with pytest.raises(ValueError):
        explicit_uncurry(curried_func, arity)
