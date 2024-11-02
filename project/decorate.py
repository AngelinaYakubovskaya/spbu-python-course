from typing import Callable, Any
from functools import wraps
import inspect
import copy
from collections import OrderedDict
import hashlib
import json


class Evaluated:
    """Class-flag for evaluating.
    If it is passed as default value of parameter then after applying smart_args
    decorator given function is evaluated every time.

    Attributes
    ----------
    func : Callable
        Function with no arguments. Returns some value.
    """

    def __init__(self, func: Callable):
        if not callable(func) or inspect.signature(func).parameters:
            raise ValueError("Evaluated requires a function with no arguments")
        self.func = func


class Isolated:
    """Fictitious class-flag."""

    pass


def smart_args(func: Callable):
    """Decorator for analyzing default values of function keyword arguments.
    Copy and/or calculate default values before executing function.

    Evaluated(func_without_args) - calculate default value before
    execution of function. func_without_args takes no argument and
    returns some value.

    Isolated - fictitious value; argument must be passed but it is
    copied (deep copy).

    Parameters
    ----------
    func : Callable
        Function which arguments will be copied/calculated.

    Raises
    ------
    AssertionError
        If Evaluated or Isolated is passed as arguments.
    ValueError
        If Isolated is passed as argument to Evaluated.
        If default value is Isolated but argument wasn't passed.

    Returns
    -------
    Function
    """
    signature = inspect.signature(func)
    params = signature.parameters

    @wraps(func)
    def wrapper(*args, **kwargs):
        # check if Evaluated or Isolated is passed as argument
        assert all(not isinstance(arg, (Evaluated, Isolated)) for arg in args)
        assert all(not isinstance(kwargs[key], (Evaluated, Isolated)) for key in kwargs)

        new_kwargs = {}
        for name, param in params.items():
            if name in kwargs and not isinstance(param.default, (Isolated, Evaluated)):
                new_kwargs[name] = kwargs[name]

            else:
                if isinstance(param.default, Evaluated):
                    d_value = param.default.func
                    if d_value == Isolated:
                        raise ValueError(
                            "Isolated was passed as argument to Evaluated."
                        )

                    if name in kwargs:
                        new_kwargs[name] = kwargs[name]
                    else:
                        new_kwargs[name] = d_value()
                if isinstance(param.default, Isolated):
                    if name in kwargs:
                        new_kwargs[name] = copy.deepcopy(kwargs[name])
                    else:
                        raise ValueError(f"Argument '{name}' must be provided")
        return func(*args, **new_kwargs)

    return wrapper


def get_hash(arg: Any) -> str:
    """Return hash value of arg."""
    json_str = json.dumps(arg, sort_keys=True, ensure_ascii=False).encode("utf8")
    return hashlib.sha256(json_str).hexdigest()


def cache_results(cache_size: int = 0):
    """Decorator for caching function results.
    Keep finite number of last input arguments and corresponding results.

    Parameters
    ----------
    cache_size : int
        Number of last results to keep.

    Returns
    -------
    Function
    """

    def decorator(func: Callable):
        cache: OrderedDict[str, str] = OrderedDict()

        @wraps(func)
        def caching(*args, **kwargs):
            key = get_hash(args), get_hash(kwargs)
            if key in cache:
                cache.move_to_end(key)
                return cache[key]

            result = func(*args, **kwargs)
            if cache_size > 0:
                if len(cache) >= cache_size:
                    oldest_key = next(iter(cache))
                    del cache[oldest_key]
                cache[key] = result
            return result

        return caching

    return decorator
