from copy import deepcopy
from collections import OrderedDict
from functools import wraps
from inspect import signature
from typing import Any, Callable, Tuple


class Isolated:
    """Indicates that a parameter should be isolated from mutation."""

    pass


class Evaluated:
    """Represents a parameter that evaluates a function only once for its default value.

    Parameters
    ----------
    function : Callable[..., Any]
        A callable that returns the value to be used as the default for the parameter.

    Raises
    ------
    TypeError
        If the provided function is an instance of Isolated.
    """

    def __init__(self, function: Callable[..., Any]) -> None:
        if isinstance(function, Isolated):
            raise TypeError("Evaluated cannot be used with Isolated.")
        self.function = function

    def compute_value(self) -> Any:
        """Returns the computed value from the function.

        Returns
        -------
        Any
            The value obtained by calling the stored function.
        """
        return self.function()


def cache_with_special_args(max_cache_size: int = 0) -> Callable:
    """Decorator to handle special parameter behaviors like Isolated and Evaluated,
       and to cache results of the function.

    Parameters
    ----------
    max_cache_size : int
        Maximum number of cached results. Defaults to 0 (no caching).
    """

    def decorator(target_function: Callable) -> Callable:
        cache_storage: OrderedDict[Tuple, Any] = OrderedDict()
        func_signature = signature(target_function)

        @wraps(target_function)
        def inner_wrapper(**input_kwargs: Any) -> Any:
            """Wrapper to manage parameter defaults, mutations, and caching.

            Parameters
            ----------
            **input_kwargs : Any
                Keyword arguments passed to the original function.

            Returns
            -------
            Any
                The result of calling the original function with adjusted parameters.
            """
            updated_params = {}

            for name, param in func_signature.parameters.items():
                if name in input_kwargs:
                    value = input_kwargs[name]
                    # Handle Isolated parameters
                    if isinstance(param.default, Isolated):
                        updated_params[name] = deepcopy(value)
                    else:
                        updated_params[name] = value

                # Handle Evaluated parameters
                elif isinstance(param.default, Evaluated):
                    updated_params[name] = param.default.compute_value()
                elif param.default is not param.empty:
                    updated_params[name] = param.default

            # Create a cache key based on the parameter values
            cache_key = (frozenset(updated_params.items()),)

            if cache_key in cache_storage:
                return cache_storage[cache_key]  # Return cached result

            result = target_function(**updated_params)  # Compute the result
            cache_storage[cache_key] = result  # Store result in cache

            # Maintain cache size
            if max_cache_size > 0 and len(cache_storage) > max_cache_size:
                cache_storage.popitem(last=False)  # Remove the oldest entry (FIFO)

            return result  # Return the computed result

        return inner_wrapper

    return decorator
