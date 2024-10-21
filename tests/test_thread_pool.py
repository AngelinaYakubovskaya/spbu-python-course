import threading
import time
import pytest
from project.thread_pool import ThreadPool


def test_task() -> None:
    """Example task for the thread pool."""
    print(f"Task executed by {threading.current_thread().name}")
    time.sleep(1)  # Simulate work


def test_thread_pool() -> None:
    """Test case to check the thread pool functionality."""
    pool = ThreadPool(3)  # Create a thread pool with 3 threads

    # Add 5 tasks to the pool
    for _ in range(5):
        pool.enqueue(test_task)

    pool.dispose()  # Close the pool and wait for task completion
    assert pool.shutdown_flag is True, "Pool should be in shutdown state after dispose."


def test_thread_count() -> None:
    """Test case to verify the correct number of threads in the pool."""
    pool = ThreadPool(5)
    assert len(pool.threads) == 5, "Incorrect number of threads created in the pool."
    pool.dispose()


def test_dispose_behavior() -> None:
    """Test case to verify the behavior of the pool after `dispose` is called."""
    pool = ThreadPool(2)
    pool.enqueue(test_task)  # Enqueue a task before disposing
    pool.dispose()  # Dispose the pool

    # Try adding a new task after the pool is disposed
    initial_size = pool.tasks.qsize()
    pool.enqueue(test_task)

    # Check that no new tasks are accepted after disposing
    assert (
        pool.tasks.qsize() == initial_size
    ), "New tasks should not be accepted after dispose."


if __name__ == "__main__":
    pytest.main()
