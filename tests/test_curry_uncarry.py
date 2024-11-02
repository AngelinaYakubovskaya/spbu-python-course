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
def test_explicit_curry_valid_cases(args, expected):
    f = explicit_curry(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    assert f(*args) == expected


def test_explicit_curry_arity_zero():
    f = explicit_curry(lambda: "No args", 0)
    assert f() == "No args"


def test_explicit_curry_arity_one():
    f = explicit_curry(lambda x: x * 2, 1)
    assert f(5) == 10


@pytest.mark.parametrize("args", [(1, 2, 3), (1, 2, 3, 4)])  # 3 & 4 arguments
def test_explicit_curry_too_many_arguments(args):
    f = explicit_curry(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        f(*args)


@pytest.mark.parametrize("arity", [-1, "a"])
def test_explicit_curry_invalid_arity(arity):
    with pytest.raises(ValueError):
        explicit_curry(lambda x: x, arity)


def test_explicit_curry_function_with_arbitrary_args():
    f = explicit_curry(print, 2)
    assert f(1)(2) is None  # print() return None


# Tests for explicit_uncurry
@pytest.mark.parametrize(
    "args, expected",
    [
        ((1, 2, 3), "<1, 2, 3>"),
        ((4, 5, 6), "<4, 5, 6>"),
    ],
)
def test_explicit_uncurry_valid_cases(args, expected):
    f = explicit_curry(lambda x, y, z: f"<{x}, {y}, {z}>", 3)
    g = explicit_uncurry(f, 3)
    assert g(*args) == expected


@pytest.mark.parametrize(
    "args",
    [
        (1,),  # 1 argument
        (1, 2, 3),  # 3 arguments
    ],
)
def test_explicit_uncurry_wrong_argument_count(args):
    f = explicit_curry(lambda x, y: x + y, 2)
    g = explicit_uncurry(f, 2)
    with pytest.raises(TypeError):
        g(*args)


@pytest.mark.parametrize("arity", [-1, "a"])
def test_explicit_uncurry_invalid_arity(arity):
    f = explicit_curry(lambda x: x, 1)
    with pytest.raises(ValueError):
        explicit_uncurry(f, arity)
