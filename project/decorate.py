import copy
import inspect
from functools import lru_cache

# Implementation of Isolated and Evaluated
def Isolated():
    """
    Returns a marker for arguments that should be passed as deep copies.

    This function is used as a marker within the smart_args decorator.
    When the decorator detects this marker, it deep copies the argument
    to ensure that changes made inside the function do not affect the
    original argument.
    """
    return IsolatedMarker()


class IsolatedMarker:
    pass


def Evaluated(func):
    """
    Returns a marker for arguments that should be evaluated at function call.

    This function is used in combination with the smart_args decorator to
    delay the evaluation of an argument until the function is called, instead
    of evaluating it at the time of function definition.

    Args:
        func (callable): The function to evaluate.

    Returns:
        EvaluatedMarker: A marker indicating delayed evaluation.
    """
    return EvaluatedMarker(func)


class EvaluatedMarker:
    def __init__(self, func):
        self.func = func


# Decorator for handling arguments with Isolated and Evaluated markers
def smart_args(func):
    """
    Decorator that processes function arguments marked with Evaluated or Isolated.

    - Arguments marked with Evaluated are computed at function call time.
    - Arguments marked with Isolated are deep-copied to prevent mutation.

    Args:
        func (callable): The function to decorate.

    Returns:
        callable: The decorated function that processes arguments based on the markers.
    """
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound_args = sig.bind_partial(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            if isinstance(value, EvaluatedMarker):
                # Evaluate the function at call time
                bound_args.arguments[name] = value.func()
            elif isinstance(value, IsolatedMarker):
                # Deep-copy the argument
                bound_args.arguments[name] = copy.deepcopy(bound_args.arguments[name])

        return func(*bound_args.args, **bound_args.kwargs)

    return wrapper


# Decorator for caching function results
def cache_results(max_size=0):
    """
    Decorator for caching function results.

    This decorator caches the results of function calls with unique argument sets.
    The maximum number of cached results is specified by max_size.

    Args:
        max_size (int): Maximum number of results to cache. If set to 0, no caching is done.

    Returns:
        callable: The decorated function with caching enabled.
    """

    def decorator(func):
        # If cache size is 0, return the original function
        if max_size == 0:
            return func
        else:
            # Use lru_cache with the given max_size
            cached_func = lru_cache(maxsize=max_size)(func)
            return cached_func

    return decorator
