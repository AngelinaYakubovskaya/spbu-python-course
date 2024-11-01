from typing import Generator, Callable, Optional

# Global instance of the prime number generator
prime_gen_instance: Optional[Generator[int, None, None]] = None
current_index = 0


def prime_generator() -> Generator[int, None, None]:
    """
    A generator that yields prime numbers in ascending order.
    Yields:
        int: The next prime number.
    """

    def is_prime(num: int) -> bool:
        """
        Checks if a number is prime.
        Args:
            num (int): The number to check.
        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


# Initialize the global generator instance once
prime_gen_instance = prime_generator()


def nth_prime_decorator(func: Callable[[int], int]) -> Callable[[int], int]:
    """
    A decorator that returns the k-th prime number.
    Args:
        func (function): The function being decorated, which will be wrapped.
    Returns:
        function: The wrapped function that returns the k-th prime number.
    """

    def wrapper(k: int) -> int:
        global current_index, prime_gen_instance

        # Initialize the generator if it's not already
        if prime_gen_instance is None:
            prime_gen_instance = prime_generator()

        # If current_index is less than k, continue yielding primes
        while current_index < k:
            prime = next(prime_gen_instance)
            current_index += 1

        # Return the last prime found (which corresponds to the k-th prime)
        return (
            prime if current_index == k else 0
        )  # Return 0 if current_index is not equal to k

    return wrapper


@nth_prime_decorator
def get_nth_prime(k: int) -> int:
    """
    A placeholder function that gets wrapped by the nth_prime_decorator.
    Args:
        k (int): The index of the prime number to return.
    Returns:
        int: The k-th prime number (determined by the decorator).
    """
    return 0  # The value will be overwritten by the decorator
