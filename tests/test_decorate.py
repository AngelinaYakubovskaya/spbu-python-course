import pytest
from project.decoratе import cache_with_special_args, Isolated, Evaluated

# Example tests for cache_with_special_args
@cache_with_special_args(max_cache_size=2)
def example_function(a: int, b: int) -> int:
    return a + b


def test_cache_with_special_args():
    assert example_function(1, 2) == 3
    assert example_function(1, 2) == 3  # Cached
    assert example_function(2, 3) == 5
    assert example_function(1, 2) == 3  # Still cached
    assert example_function(3, 4) == 7  # Evicts (1, 2)
    assert example_function(1, 2) == 3  # Recompute


# Tests for Isolated and Evaluated
def test_isolated():
    f = lambda x, y=Isolated(): x + y
    assert f(1, 2) == 3
    assert f(1, 2) == 3  # The second argument is isolated


def test_evaluated():
    f = Evaluated(lambda: 42)
    assert f.compute_value() == 42


def test_evaluated_error():
    with pytest.raises(TypeError):
        Evaluated(Isolated())
