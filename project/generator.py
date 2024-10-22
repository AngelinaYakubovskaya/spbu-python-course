from typing import Generator, Callable

prime_gen_instance = None  # Инициализируем переменную


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


# Теперь мы можем инициализировать экземпляр после определения функции
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
        """
        A wrapper function to find the k-th prime number.

        Args:
            k (int): The index of the prime number to return.

        Returns:
            int: The k-th prime number.
        """
        # Используем глобальный экземпляр prime_gen_instance
        global prime_gen_instance

        # Генератор уже запущен, продолжаем получать значения
        for idx in range(k):
            prime = next(prime_gen_instance)
        return prime

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
    pass
