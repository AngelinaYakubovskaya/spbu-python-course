import pytest
from project.curry_uncarry import curry_explicit, uncurry_explicit


def test_zero_arity_function():
    """Test for currying a zero-arity function."""
    zero_arity_function = curry_explicit(lambda: "no args", 0)
    assert zero_arity_function() == "no args"


def test_curry_and_uncurry():
    """Test currying and uncurrying a function with multiple parameters."""
    f = lambda x, y, z: f"<{x},{y},{z}>"
    curried = curry_explicit(f, 3)
    uncurried = uncurry_explicit(curried, 3)

    assert curried(123)(456)(789) == "<123,456,789>"
    assert uncurried(123, 456, 789) == "<123,456,789>"


def test_invalid_arity():
    """Test for invalid arity."""
    with pytest.raises(ValueError):
        curry_explicit(lambda x: x, -1)
    with pytest.raises(ValueError):
        uncurry_explicit(lambda x: x, -1)


def test_too_many_arguments():
    """Test for too many arguments provided."""
    curried = curry_explicit(lambda x, y: x + y, 2)
    with pytest.raises(TypeError):
        curried(1)(2)(3)
