from functools import wraps


def curry_explicit(function, arity):
    """Transforms a function into a curried version with a specified arity."""
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    # Для функции нулевой арности возвращаем её сразу
    if arity == 0:
        return function

    @wraps(function)
    def curried_function(*args):
        if len(args) > arity:
            raise TypeError("Too many arguments provided")
        if len(args) == arity:
            return function(*args)
        return lambda x: curried_function(*args, x)

    return curried_function


def uncurry_explicit(function, arity):
    """Transforms a curried function back into a function that accepts all arguments at once."""
    if not isinstance(arity, int) or arity < 0:
        raise ValueError("Arity must be a non-negative integer")

    @wraps(function)
    def uncurried_function(*args):
        if len(args) != arity:
            raise TypeError(f"Expected {arity} arguments, but got {len(args)}")
        result = function
        for arg in args:
            result = result(arg)
        return result

    return uncurried_function
