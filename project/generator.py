from typing import Generator, Callable, Optional, List

# Global cache for storing previously generated primes
prime_cache: List[int] = []


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


def nth_prime_decorator(func: Callable[[int], int]) -> Callable[[int], int]:
    """
    A decorator that returns the k-th prime number using caching to store previously generated primes.
    Args:
        func (function): The function being decorated, which will be wrapped.
    Returns:
        function: The wrapped function that returns the k-th prime number.
    """

    def wrapper(k: int) -> int:
        global prime_cache

        # Generate primes until we reach at least the k-th prime
        prime_gen = prime_generator()
        while len(prime_cache) < k:
            prime_cache.append(next(prime_gen))

        # Return the k-th prime (1-indexed)
        return prime_cache[k - 1]

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
