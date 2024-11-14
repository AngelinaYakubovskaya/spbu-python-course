from functools import wraps
from typing import Callable, Any, List


def curry_explicit(func: Callable, arity: int) -> Callable:
    """Decorator for transforming a given function into a curried version.

    Currying is the process of breaking down a function that takes multiple
    arguments into a series of functions that each take a single argument.

    Note: This implementation does not support keyword arguments.

    Parameters
    ----------
    func : Callable
        The function to be transformed into a curried form.
    arity : int
        The number of parameters that the original function accepts.

    Raises
    ------
    ValueError
        If the specified arity is negative.
    TypeError
        If the original function takes zero arguments but an argument is provided.

    Returns
    -------
    Callable
        A curried version of the input function.
    """
    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    args: List[Any] = []

    @wraps(func)
    def curry_func(arg=None):
        if arity == 0 and arg is not None:
            raise TypeError("Arity is 0 but an argument was given.")
        if arity == 0:
            return func()
        if len(args) > arity:
            raise TypeError("Inappropriate number of arguments.")
        if arg is not None:
            args.append(arg)
        if len(args) == arity:
            return func(*args)
        else:
            return curry_func

    return curry_func


def uncurry_explicit(func: Callable, arity: int) -> Callable:
    """Decorator for transforming a curried function back to its uncurried form.

    This is the inverse of the `curry_explicit` decorator, allowing the
    original function to accept multiple arguments again.

    Note: This implementation does not support keyword arguments.

    Parameters
    ----------
    func : Callable
        The curried function to be transformed back to its uncurried form.
    arity : int
        The number of parameters that the original function accepts.

    Raises
    ------
    ValueError
        If the specified arity is negative.
    TypeError
        If the number of provided arguments does not match the expected arity.

    Returns
    -------
    Callable
        The uncurried version of the input function.
    """
    if arity < 0:
        raise ValueError("Arity cannot be negative.")

    @wraps(func)
    def uncurry_func(*args):
        if arity != len(args):
            raise TypeError("Inappropriate number of arguments.")

        if arity == 0:
            return func()
        uncurried = func
        for arg in args:
            uncurried = uncurried(arg)

        return uncurried

    return uncurry_func
