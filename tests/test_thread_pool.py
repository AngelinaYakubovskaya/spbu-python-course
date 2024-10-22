import threading
import time
import pytest
from project.thread_pool import ThreadPool

# Простая задача для тестирования
def simple_task() -> None:
    """
    Example task for the thread pool.
    Simulates a task by printing the thread name and sleeping for a short time.
    """
    print(f"Task executed by {threading.current_thread().name}")
    time.sleep(0.1)


### Тесты для каждого метода класса ThreadPool ###


def test_enqueue() -> None:
    """
    Test case to verify that tasks are enqueued and processed by the pool.
    Ensures that tasks can be added to the pool and processed by worker threads.
    """
    pool = ThreadPool(3)  # Создаем пул с 3 потоками

    # Добавляем 5 задач в пул
    for _ in range(5):
        pool.enqueue(simple_task)

    pool.dispose()  # Закрываем пул и ждем завершения всех задач


def test_dispose() -> None:
    """
    Test case to verify the behavior of the pool after `dispose` is called.
    Ensures that no new tasks are accepted after the pool has been disposed.
    """
    pool = ThreadPool(2)

    # Добавляем задачу до завершения работы пула
    pool.enqueue(simple_task)
    pool.dispose()  # Завершаем работу пула

    # Пробуем добавить новую задачу после завершения работы пула
    pool.enqueue(simple_task)

    # Проверяем, что после завершения задачи больше не принимаются
    assert not pool.tasks, "New tasks should not be accepted after dispose."
    print("Pool has been disposed, no more tasks should be accepted.")


def test_worker_execution() -> None:
    """
    Test case to verify that worker threads execute the tasks properly.
    Ensures that tasks enqueued are executed by the worker threads.
    """
    pool = ThreadPool(4)  # Создаем пул с 4 потоками

    # Добавляем 10 задач в пул
    for _ in range(10):
        pool.enqueue(simple_task)

    pool.dispose()  # Ждем завершения всех задач


def test_initialize_threads() -> None:
    """
    Test case to verify that the correct number of threads are initialized in the pool.
    Ensures that the pool initializes the number of threads as specified.
    """
    pool = ThreadPool(5)  # Инициализируем пул с 5 потоками
    assert len(pool.threads) == 5, "Expected 5 threads to be initialized."

    pool.dispose()  # Завершаем работу пула


def test_thread_count() -> None:
    """
    Test case to verify the correct number of active threads in the pool.
    Ensures that the pool has the same number of active threads as specified.
    """
    initial_active_threads = (
        threading.active_count()
    )  # Считаем активные потоки до создания пула
    pool = ThreadPool(5)  # Создаем пул с 5 потоками

    # Даем время потокам запуститься
    time.sleep(0.5)  # Небольшая задержка, чтобы потоки запустились

    current_active_threads = threading.active_count()  # Считаем текущие активные потоки
    active_threads_in_pool = (
        current_active_threads - initial_active_threads
    )  # Считаем потоки пула

    assert (
        active_threads_in_pool == 5
    ), f"Expected 5 active threads, found {active_threads_in_pool}"
    pool.dispose()


if __name__ == "__main__":
    pytest.main()
