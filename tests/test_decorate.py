import pytest
import random
from project.decorate import smart_args, Isolated, Evaluated


@smart_args
def check_isolation(*, d=Isolated()):
    """
    Test function to check the behavior of Isolated arguments.

    Modifies a dictionary by setting the key 'a' to 0, but due to the use
    of the `Isolated` marker, the original dictionary will not be modified.

    Parameters:
        d (dict, optional): A dictionary to modify. If not provided, the
                            argument is deep-copied from the default value.

    Returns:
        dict: The modified dictionary with 'a' set to 0.
    """
    d["a"] = 0
    return d


@smart_args
def check_evaluation(
    *, x=random.randint(0, 100), y=Evaluated(lambda: random.randint(0, 100))
):
    """
    Test function to check the behavior of Evaluated arguments.

    Returns two values. The first value `x` is computed when the function
    is defined, and the second value `y` is evaluated at the time of
    function call.

    Parameters:
        x (int, optional): A random number, evaluated at function definition.
        y (int, optional): A random number, evaluated at function call using
                           the Evaluated marker. Can be manually overridden.

    Returns:
        tuple: A tuple containing the values of x and y.
    """
    return x, y


def test_check_isolation():
    """Test for Isolated marker functionality to ensure deep-copying of mutable args."""
    original_dict = {"a": 10}
    result = check_isolation(d=original_dict)
    assert result == {"a": 0}  # Проверяем, что 'a' установлено в 0 в копии
    assert original_dict == {"a": 10}  # Оригинальный словарь не изменен


def test_check_evaluation():
    """Test for Evaluated marker functionality to ensure lazy evaluation."""
    result1 = check_evaluation()
    result2 = check_evaluation()
    assert result1[0] == result2[0]  # `x` остается постоянным
    assert result1[1] != result2[1]  # `y` изменяется между вызовами
