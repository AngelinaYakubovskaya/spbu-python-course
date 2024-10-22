def prime_generator():
    """
    A generator that yields prime numbers in ascending order.

    Yields:
        int: The next prime number.
    """

    def is_prime(num):
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


# Создаем экземпляр генератора
gen = prime_generator()


def nth_prime_decorator(func):
    """
    A decorator that returns the k-th prime number.

    Args:
        func (function): The function being decorated, which will be wrapped.

    Returns:
        function: The wrapped function that returns the k-th prime number.
    """

    def wrapper(k):
        """
        A wrapper function to find the k-th prime number.

        Args:
            k (int): The index of the prime number to return.

        Returns:
            int: The k-th prime number.
        """
        prime = None
        for _ in range(k):
            prime = next(gen)  # Используем общий экземпляр генератора
        return prime

    return wrapper


@nth_prime_decorator
def get_nth_prime(k):
    """
    A placeholder function that gets wrapped by the nth_prime_decorator.

    Args:
        k (int): The index of the prime number to return.

    Returns:
        int: The k-th prime number (determined by the decorator).
    """
    pass
