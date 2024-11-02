from typing import Callable, Any
from functools import wraps
import inspect
import copy
from collections import OrderedDict
import hashlib
import json


class Evaluated:
    """Class used as a flag for deferred evaluation of function arguments.

    When an instance of this class is passed as a default value for a parameter,
    the associated function will be evaluated each time the decorated function is called.

    Attributes
    ----------
    func : Callable
        A callable that takes no arguments and returns a value.
    """

    def __init__(self, func: Callable):
        if not callable(func) or inspect.signature(func).parameters:
            raise ValueError("Evaluated requires a function with no arguments.")
        self.func = func


class Isolated:
    """A class used as a flag to indicate that a parameter should be deeply copied.

    This class is not meant to hold any state or behavior; it's a marker.
    """


def smart_args(func: Callable) -> Callable:
    """Decorator that analyzes the default values of function keyword arguments.

    It allows for the copying and/or calculation of default values before the function executes.

    Usage:
    - Evaluated(func_without_args) - Calculates the default value before execution.
      The `func_without_args` must take no arguments and return a value.
    - Isolated - Indicates that an argument should be copied (deep copy) if provided.

    Parameters
    ----------
    func : Callable
        The function whose arguments will be processed for copying or calculating defaults.

    Raises
    ------
    AssertionError
        If an instance of Evaluated or Isolated is passed as a positional or keyword argument.
    ValueError
        If Isolated is passed as an argument to Evaluated.
        If a default value is Isolated but the corresponding argument is not provided.

    Returns
    -------
    Callable
        A wrapper function that applies the specified logic to the original function.
    """
    signature = inspect.signature(func)
    params = signature.parameters

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Assert that no Evaluated or Isolated instances are passed as arguments
        assert all(
            not isinstance(arg, (Evaluated, Isolated)) for arg in args
        ), "Arguments cannot be instances of Evaluated or Isolated."
        assert all(
            not isinstance(kwargs[key], (Evaluated, Isolated)) for key in kwargs
        ), "Keyword arguments cannot be instances of Evaluated or Isolated."

        new_kwargs = {}
        for name, param in params.items():
            if name in kwargs and not isinstance(param.default, (Isolated, Evaluated)):
                new_kwargs[name] = kwargs[name]

            else:
                if isinstance(param.default, Evaluated):
                    d_value = param.default.func
                    if d_value == Isolated:
                        raise ValueError(
                            "Isolated cannot be passed as an argument to Evaluated."
                        )

                    if name in kwargs:
                        new_kwargs[name] = kwargs[name]
                    else:
                        new_kwargs[name] = d_value()
                if isinstance(param.default, Isolated):
                    if name in kwargs:
                        new_kwargs[name] = copy.deepcopy(kwargs[name])
                    else:
                        raise ValueError(f"Argument '{name}' must be provided.")
        return func(*args, **new_kwargs)

    return wrapper


def get_hash(arg: Any) -> str:
    """Compute the SHA-256 hash of a given argument.

    Parameters
    ----------
    arg : Any
        The argument to hash, which can be of any serializable type.

    Returns
    -------
    str
        The hexadecimal representation of the hash value.
    """
    json_str = json.dumps(arg, sort_keys=True, ensure_ascii=False).encode("utf8")
    return hashlib.sha256(json_str).hexdigest()


def cache_results(cache_size: int = 0) -> Callable:
    """Decorator for caching the results of a function.

    This decorator maintains a finite number of the most recent input arguments
    and their corresponding results.

    Parameters
    ----------
    cache_size : int
        The maximum number of cached results to retain. A value of 0 disables caching.

    Returns
    -------
    Callable
        A wrapper function that manages caching behavior.
    """

    def decorator(func: Callable) -> Callable:
        cache: OrderedDict[str, str] = OrderedDict()

        @wraps(func)
        def caching(*args, **kwargs):
            key = get_hash(args), get_hash(kwargs)
            if key in cache:
                cache.move_to_end(key)  # Mark as recently used
                return cache[key]

            result = func(*args, **kwargs)
            if cache_size > 0:
                if len(cache) >= cache_size:
                    oldest_key = next(iter(cache))  # Get the oldest cached item
                    del cache[oldest_key]  # Remove the oldest item
                cache[key] = result  # Cache the new result
            return result

        return caching

    return decorator
