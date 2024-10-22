# Создаем один раз экземпляр генератора на уровне модуля
prime_gen_instance = prime_generator()


def prime_generator() -> "Generator[int, None, None]":
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


def nth_prime_decorator(func: "Callable[[int], None]") -> "Callable[[int], int]":
    """
    A decorator that returns the k-th prime number using a single generator instance.

    Args:
        func (Callable[[int], None]): The function being decorated, which will be wrapped.

    Returns:
        Callable[[int], int]: The wrapped function that returns the k-th prime number.
    """

    def wrapper(k: int) -> int:
        """
        A wrapper function to find the k-th prime number.

        Args:
            k (int): The index of the prime number to return.

        Returns:
            int: The k-th prime number.
        """
        # Используем уже созданный экземпляр генератора
        for _ in range(k):
            prime = next(prime_gen_instance)
        return prime

    return wrapper


@nth_prime_decorator
def get_nth_prime(k: int) -> None:
    """
    A placeholder function that gets wrapped by the nth_prime_decorator.

    Args:
        k (int): The index of the prime number to return.

    Returns:
        None: Since the actual return value is determined by the decorator.
    """
    pass
