import pytest
from project.generator import get_nth_prime, prime_generator


@pytest.fixture
def prime_gen():
    """Fixture to create a new instance of prime number generator."""
    return prime_generator()


@pytest.mark.parametrize(
    "k, expected_prime",
    [
        (1, 2),  # 1st prime number is 2
        (2, 3),  # 2nd prime number is 3
        (3, 5),  # 3rd prime number is 5
        (4, 7),  # 4th prime number is 7
        (5, 11),  # 5th prime number is 11
    ],
)
def test_nth_prime_decorator(k, expected_prime):
    """Test to check if the nth_prime_decorator returns the correct prime."""
    assert get_nth_prime(k) == expected_prime


def test_prime_generator(prime_gen):
    """Test prime generator function for first 5 primes."""
    expected_primes = [2, 3, 5, 7, 11]
    generated_primes = [next(prime_gen) for _ in range(5)]
    assert generated_primes == expected_primes


def test_repeat_prime_request():
    """Test requesting the same prime number multiple times."""
    second_prime_first_call = get_nth_prime(2)  # Запрашиваем второе простое число
    second_prime_second_call = get_nth_prime(
        2
    )  # Снова запрашиваем второе простое число

    # Убедимся, что оба вызова возвращают одно и то же значение
    assert second_prime_first_call == second_prime_second_call
    assert second_prime_first_call == 3  # Второе простое число — это 3
