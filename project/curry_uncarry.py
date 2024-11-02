from typing import Callable, Any


def explicit_curry(
    original_func: Callable[..., Any], expected_arity: int
) -> Callable[..., Any]:
    """
    Curries a function to accept one argument at a time.

    Parameters
    ----------
    original_func : Callable[..., Any]
        The function to be curried.
    expected_arity : int
        The number of arguments the original function requires.

    Returns
    -------
    Callable[..., Any]
        A curried version of the original function.

    Raises
    ------
    ValueError
        If expected_arity is not a non-negative integer.
    TypeError
        If too many arguments are provided when calling the curried function.
    """
    if not isinstance(expected_arity, int) or expected_arity < 0:
        raise ValueError("Expected arity must be a non-negative integer.")

    def curried(*provided_args: Any) -> Any:
        arg_count = len(provided_args)
        if arg_count > expected_arity:
            raise TypeError(
                f"Too many arguments: expected at most {expected_arity}, got {arg_count}."
            )

        if arg_count == expected_arity:
            return original_func(*provided_args)

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
    Callable[..., Any]
        The uncurried version of the function.

    Raises
    ------
    ValueError
        If expected_arity is not a non-negative integer.
    TypeError
        If the number of arguments provided does not match the expected arity.
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
