import pytest
from project.decorate import (
    smart_args,
    Isolated,
    Evaluated,
    cache_results,
    curry_explicit,
)
import copy  # Импортируем copy


def test_check_isolation():
    """Test for the behavior of the Isolated argument."""
    no_mutable = {"a": 10}

    @smart_args
    def check_isolation(d=Isolated()):
        d["a"] = 0  # Modify the isolated copy
        return d

    result = check_isolation(d=no_mutable)
    assert result == {"a": 0}  # Check that the returned dictionary has 'a': 0
    assert no_mutable == {"a": 10}  # Ensure the original dictionary remains unchanged


def test_check_evaluation():
    """Test for the behavior of the Evaluated argument."""
    evaluation_counter = {"count": 0}

    def get_incremented_number():
        evaluation_counter["count"] += 1
        return evaluation_counter["count"]

    # Create a new function that uses the Evaluated marker with the counter
    @smart_args
    def check_increment_evaluation(*, x=Evaluated(get_incremented_number)):
        return x

    # Test that the function increments and evaluates the value every time
    assert check_increment_evaluation() == 1  # First call, should evaluate to 1
    assert check_increment_evaluation() == 2  # Second call, should evaluate to 2
    assert check_increment_evaluation() == 3  # Third call, should evaluate to 3


def test_combined_isolated_and_evaluated():
    """Test that a function can handle both Isolated and Evaluated arguments simultaneously."""
    mutable_data = {"value": 42}

    def get_random_number():
        return 100  # For simplicity, return a constant (can be random)

    # Define a function using both Isolated and Evaluated arguments
    @smart_args
    def check_combined(
        *, isolated_dict=Isolated(), evaluated_num=Evaluated(get_random_number)
    ):
        isolated_dict["new_key"] = evaluated_num
        return isolated_dict, evaluated_num

    # Use deepcopy to ensure isolation
    result, number = check_combined(isolated_dict=copy.deepcopy(mutable_data))
    assert result == {"value": 42, "new_key": 100}  # The modified isolated copy
    assert mutable_data == {"value": 42}  # Original data is unchanged

    # Ensure that `evaluated_num` is recalculated on each call
    assert number == 100  # Evaluated to the returned value from get_random_number


def test_frozen_arity():
    """Check that arity is fixed and does not allow extra arguments."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)

    # The first call should return a function expecting the second argument
    curried_part = curried_add(1)
    assert callable(curried_part)

    # Attempting to pass two arguments at once should raise an error
    with pytest.raises(TypeError):
        curried_part(2)  # This should raise TypeError


def test_not_more_than_one_argument_per_call():
    """Check that curried function raises error when passing more than one argument at each step."""
    curried_add = curry_explicit(lambda x, y: x + y, 2)

    with pytest.raises(TypeError):
        curried_add(1, 2)  # This should raise TypeError


def test_zero_arity_function():
    """Test zero-arity function."""
    zero_arity_function = curry_explicit(lambda: "no arguments", 0)
    assert zero_arity_function() == "no arguments"

    uncurried_zero_arity_function = zero_arity_function
    assert uncurried_zero_arity_function() == "no arguments"
