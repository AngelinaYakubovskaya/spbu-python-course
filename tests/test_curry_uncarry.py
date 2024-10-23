import pytest
from project.curry_uncarry import curry_explicit, uncurry_explicit


def test_curry_function():
    """Test the curried function with a simple lambda."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    assert curried_add(3)(4) == 7  # Test curried function with two arguments


def test_uncurry_function():
    """Test the uncurried function."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    uncurried_add = uncurry_explicit(curried_add, 2)
    assert uncurried_add(5, 7) == 12  # Test uncurried function with two arguments


def test_built_in_function():
    """Test currying with a built-in function."""
    curried_print = curry_explicit(print, 2)
    assert curried_print(1)(2) is None  # `print` returns None, and it's arity is fixed


def test_frozen_arity():
    """Test that the arity is frozen and does not allow more arguments."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)

    # First function call should return a function waiting for the second argument
    curried_part = curried_add(1)
    assert callable(curried_part)

    # Trying to pass two arguments at once should raise an error
    with pytest.raises(TypeError):
        curried_add(1, 2)

    # Now the second argument can be passed separately
    assert curried_part(5) == 6  # (1 + 5)


def test_no_more_than_one_argument_per_call():
    """Test that the curried function raises an error when more than one argument is passed per step."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)

    with pytest.raises(TypeError):
        curried_add(
            1, 2
        )  # Passing more than one argument at a time should raise an error

    with pytest.raises(TypeError):
        curried_add(1)(2, 3)  # Passing more than one argument in the second step


def test_uncurried_exceeds_arity():
    """Test that uncurried functions raise an error when called with more or fewer arguments than expected."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)
    uncurried_add = uncurry_explicit(curried_add, 2)

    with pytest.raises(TypeError):
        uncurried_add(1)  # Fewer arguments than expected

    with pytest.raises(TypeError):
        uncurried_add(1, 2, 3)  # More arguments than expected


def test_zero_arity_function():
    """Test curry and uncurry with zero arity function."""
    zero_arity_function = curry_explicit(lambda: "no args", 0)
    assert zero_arity_function() == "no args"

    uncurried_zero_arity_function = uncurry_explicit(zero_arity_function, 0)
    assert uncurried_zero_arity_function() == "no args"


def test_higher_arity_function():
    """Test a curried function with more than two arguments."""
    curried_concat = curry_explicit(lambda x, y, z: f"{x}{y}{z}", 3)

    # Currying step by step
    step1 = curried_concat("A")
    step2 = step1("B")
    assert step2("C") == "ABC"

    # Currying directly
    assert curried_concat("X")("Y")("Z") == "XYZ"

    # Uncurrying
    uncurried_concat = uncurry_explicit(curried_concat, 3)
    assert uncurried_concat("D", "E", "F") == "DEF"
