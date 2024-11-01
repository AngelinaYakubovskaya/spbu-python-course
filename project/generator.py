from typing import Generator, Callable, List

# Global cache to store computed prime numbers
prime_cache: List[int] = []


def prime_generator() -> Generator[int, None, None]:
    """
    A generator that yields prime numbers in ascending order.

    Yields:
        int: The next prime number in the sequence.
    """

    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.

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
    A decorator to retrieve the k-th prime number, using a cache for
    efficient repeated access to previously computed primes.

    Args:
        func (Callable[[int], int]): The function to decorate.

    Returns:
        Callable[[int], int]: A wrapped function that returns the k-th prime number.
    """
    prime_gen_instance = prime_generator()  # Local instance of the prime generator

    def wrapper(k: int) -> int:
        """
        Retrieve the k-th prime number, using cached values if available.

        Args:
            k (int): The index of the desired prime number (1-based index).

        Returns:
            int: The k-th prime number.

        Raises:
            ValueError: If k is not a positive integer.
        """
        if k <= 0:
            raise ValueError("Index must be a positive integer.")

        # Ensure the cache contains at least k primes
        while len(prime_cache) < k:
            prime_cache.append(next(prime_gen_instance))
        return prime_cache[k - 1]

    return wrapper


@nth_prime_decorator
def get_nth_prime(k: int) -> int:
    """
    A placeholder function wrapped by nth_prime_decorator to retrieve
    the k-th prime number.

    Args:
        k (int): The index of the desired prime number (1-based index).

    Returns:
        int: The k-th prime number, returned by the decorator.
    """
    return 0  # This return is overridden by the decorator
