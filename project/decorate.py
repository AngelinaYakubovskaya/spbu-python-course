import copy
import inspect
import random


def Isolated():
    """Marker for arguments that should be deep-copied before function execution."""
    return None


class Evaluated:
    """Marker for arguments that should be evaluated at the time of function execution."""

    def __init__(self, func):
        self.func = func

    def evaluate(self):
        """Evaluate the function and return its result."""
        return self.func()


def get_random_number():
    """Returns a random integer between 0 and 100."""
    return random.randint(0, 100)


def smart_args(func):
    """
    Decorator to process arguments marked as `Evaluated` or `Isolated`.
    Arguments marked as `Isolated` will be deep-copied, and those marked as
    `Evaluated` will be executed at the time of function call.
    """
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        # Iterate through bound arguments to apply Isolated and Evaluated logic
        for param_name, value in bound_args.arguments.items():
            param = sig.parameters[param_name]
            if isinstance(param.default, Evaluated) and param_name not in kwargs:
                bound_args.arguments[param_name] = param.default.evaluate()
            elif isinstance(param.default, Isolated) or (
                value is None and param.default is None
            ):
                bound_args.arguments[param_name] = copy.deepcopy(value)

        return func(*bound_args.args, **bound_args.kwargs)

    return wrapper
