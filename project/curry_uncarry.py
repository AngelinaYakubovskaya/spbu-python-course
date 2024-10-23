from functools import wraps


def curry_explicit(function, arity):
    """
    Transforms a function into a curried version with a specified arity.

    Currying transforms a function that takes multiple arguments into
    a series of functions that each take one argument.

    Args:
        function (callable): The function to be curried.
        arity (int): The number of arguments the function expects (its arity).

    Returns:
        callable: A curried version of the original function that can be called
                  successively with single arguments until all arguments are provided.

    Raises:
        ValueError: If arity is not a non-negative integer.
        TypeError: If more than one argument is passed to any curried function call.
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    if arity == 0:
        return lambda: function()

    def curry(*args):
        if len(args) > arity:
            raise TypeError(f"Function expected {arity} arguments, got {len(args)}")
        if len(args) == arity:
            return function(*args)
        return lambda *more_args: curry(*(args + more_args))

    return curry


def uncurry_explicit(function, arity):
    """
    Transforms a curried function back into a regular function with a specified arity.

    Uncurrying is the reverse of currying. It transforms a series of function calls,
    each taking a single argument, back into a function that takes all arguments at once.

    Args:
        function (callable): The curried function to be uncurried.
        arity (int): The number of arguments the original function expects.

    Returns:
        callable: A function that accepts all arguments at once.

    Raises:
        ValueError: If arity is not a non-negative integer.
        TypeError: If the uncurried function is called with an incorrect number of arguments.
    """
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    def uncurry(*args):
        if len(args) != arity:
            raise TypeError(f"Expected {arity} arguments, got {len(args)}")
        result = function
        for arg in args:
            result = result(arg)
        return result

    return uncurry

    return uncurried
