from typing import Generator, Callable, Optional

# Глобальный экземпляр генератора простых чисел
prime_gen_instance: Optional[Generator[int, None, None]] = None
current_index: int = 0  # Отслеживает текущий индекс для последовательности


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


# Инициализация глобального экземпляра генератора один раз
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
        global current_index, prime_gen_instance

        # Убедимся, что prime_gen_instance не равен None
        if prime_gen_instance is None:
            prime_gen_instance = prime_generator()

        # Получаем k-е простое число, начиная с текущего индекса
        prime: int = 0
        for _ in range(current_index, k):
            prime = next(prime_gen_instance)
            current_index += 1  # Обновляем текущий индекс
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
    # Возвращаемое значение теперь управляется декоратором
    return k  # Возвращает значение, установленное декоратором
