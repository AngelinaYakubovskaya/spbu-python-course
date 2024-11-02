from copy import deepcopy
from collections import OrderedDict
from functools import wraps
from inspect import signature
from typing import Any, Callable, Tuple


class Isolated:
    """Indicates that a parameter should be isolated from mutation."""

    pass


class Evaluated:
    """Represents a parameter that evaluates a function only once for its default value."""

    def __init__(self, function: Callable[..., Any]) -> None:
        if isinstance(function, Isolated):
            raise TypeError("Evaluated cannot be used with Isolated.")
        self.function = function

    def compute_value(self) -> Any:
        """Returns the computed value from the function."""
        return self.function()


def cache_with_special_args(max_cache_size: int = 0) -> Callable:
    """Decorator to handle special parameter behaviors and cache results of the function."""

    def decorator(target_function: Callable) -> Callable:
        cache_storage: OrderedDict[Tuple, Any] = OrderedDict()
        func_signature = signature(target_function)

        @wraps(target_function)
        def inner_wrapper(**input_kwargs: Any) -> Any:
            updated_params = {}
            for name, param in func_signature.parameters.items():
                if name in input_kwargs:
                    value = input_kwargs[name]
                    if isinstance(param.default, Isolated):
                        updated_params[name] = deepcopy(value)
                    else:
                        updated_params[name] = value
                elif isinstance(param.default, Evaluated):
                    updated_params[name] = param.default.compute_value()
                elif param.default is not param.empty:
                    updated_params[name] = param.default

            cache_key = frozenset(updated_params.items())
            if cache_key in cache_storage:
                return cache_storage[cache_key]

            result = target_function(**updated_params)
            cache_storage[cache_key] = result

            if max_cache_size > 0 and len(cache_storage) > max_cache_size:
                cache_storage.popitem(last=False)

            return result

        return inner_wrapper

    return decorator
