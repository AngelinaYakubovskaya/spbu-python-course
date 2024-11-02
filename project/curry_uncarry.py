from typing import Callable, Any


def explicit_curry(
    original_func: Callable[..., Any], expected_arity: int
) -> Callable[..., Any]:
    """
    Curries a function to accept one argument at a time, returning a function that
    collects subsequent arguments until the total count equals the expected arity.

    Parameters
    ----------
    original_func : Callable[..., Any]
        The function to be curried.
    expected_arity : int
        The number of arguments the original function requires.

    Returns
    -------
    curried_function : Callable[..., Any]
        A curried version of the original function.

    Raises
    ------
    ValueError
        If expected_arity is not a non-negative integer.
    TypeError
        If too many arguments are provided when calling the curried function.

    Examples
    --------
    >>> curried_function = explicit_curry(lambda x, y, z: f'<{x}, {y}, {z}>', 3)
    >>> curried_function(1)(2)(3)
    '<1, 2, 3>'
    """
    if not isinstance(expected_arity, int) or expected_arity < 0:
        raise ValueError("Expected arity must be a non-negative integer.")

    def curried(*provided_args: Any) -> Any:
        if len(provided_args) > expected_arity:
            raise TypeError(
                f"Too many arguments: expected at most {expected_arity}, got {len(provided_args)}."
            )

        # Call the original function if we have enough arguments
        if len(provided_args) == expected_arity:
            return original_func(*provided_args)

        # Return a new function for additional arguments
        return lambda *additional_args: curried(*(provided_args + additional_args))

    return curried


def explicit_uncurry(
    curried_function: Callable[..., Any], expected_arity: int
) -> Callable[..., Any]:
    """
    Converts a curried function so that it can accept all arguments at once.

    Parameters
    ----------
    curried_function : Callable[..., Any]
        The curried function to be uncurried.
    expected_arity : int
        The number of arguments the original function requires.

    Returns
    -------
    uncurried_function : Callable[..., Any]
        The uncurried version of the function.

    Raises
    ------
    ValueError
        If expected_arity is not a non-negative integer.
    TypeError
        If the number of arguments provided does not match the expected arity.

    Examples
    --------
    >>> curried_function = explicit_curry(lambda x, y, z: f'<{x}, {y}, {z}>', 3)
    >>> uncurried_function = explicit_uncurry(curried_function, 3)
    >>> uncurried_function(1, 2, 3)
    '<1, 2, 3>'
    """
    if not isinstance(expected_arity, int) or expected_arity < 0:
        raise ValueError("Expected arity must be a non-negative integer.")

    def uncurried(*args: Any) -> Any:
        if len(args) != expected_arity:
            raise TypeError(
                f"Expected exactly {expected_arity} arguments, but got {len(args)}."
            )

        return curried_function(*args)

    return uncurried
