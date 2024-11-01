from typing import Generator, Callable, List

# Глобальный кэш для хранения простых чисел
prime_cache: List[int] = []


def prime_generator() -> Generator[int, None, None]:
    """
    Генератор, который выдает простые числа в возрастающем порядке.
    Yields:
        int: Следующее простое число.
    """

    def is_prime(num: int) -> bool:
        """Проверяет, является ли число простым."""
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
    Декоратор, который возвращает k-е простое число, используя кэш для хранения
    уже найденных простых чисел.
    """
    prime_gen_instance = prime_generator()  # Локальная инициализация генератора

    def wrapper(k: int) -> int:
        if k <= 0:
            raise ValueError("Index must be a positive integer.")

        # Проверка, если нужное количество простых чисел уже в кэше
        while len(prime_cache) < k:
            prime_cache.append(next(prime_gen_instance))
        return prime_cache[k - 1]

    return wrapper


@nth_prime_decorator
def get_nth_prime(k: int) -> int:
    """
    Заглушка функции, которая оборачивается декоратором для получения k-го простого числа.
    """
    return 0  # Это значение будет переопределено декоратором
