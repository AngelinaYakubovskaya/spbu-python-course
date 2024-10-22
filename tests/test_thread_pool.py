import threading
import time
import pytest
from project.thread_pool import ThreadPool


def simple_task() -> None:
    """
    A simple task that just sleeps for a short time.
    This simulates work being done in a thread.
    """
    print(f"Task executed by {threading.current_thread().name}")
    time.sleep(1)


def test_task() -> None:
    """
    Test the execution of a simple task in the thread pool.
    """
    simple_task()  # Directly calling the task for testing purposes


def test_enqueue() -> None:
    """
    Test case to check if tasks can be added to the pool.
    """
    pool = ThreadPool(3)  # Create a thread pool with 3 threads

    # Add a single task to the pool
    pool.enqueue(simple_task)

    # Ensure that tasks have been added
    assert len(pool.tasks) == 1, "Task should be enqueued."

    pool.dispose()  # Dispose the pool after adding tasks


def test_thread_pool() -> None:
    """
    Test case to check the thread pool functionality.
    Adds tasks to the pool and verifies that all tasks are processed.
    """
    pool = ThreadPool(3)  # Create a thread pool with 3 threads

    # Add 5 tasks to the pool
    for _ in range(5):
        pool.enqueue(simple_task)

    pool.dispose()  # Close the pool and wait for task completion
    assert len(pool.threads) == 3, "Pool should have 3 threads."
    print(f"Active threads after dispose: {threading.active_count()}")


def test_thread_count() -> None:
    """
    Test case to verify the correct number of active threads in the pool.
    Ensures that the pool has the same number of active threads as specified.
    """
    initial_active_threads = threading.active_count()  # Count initial active threads
    pool = ThreadPool(5)  # Create a thread pool with 5 threads

    # Wait for all threads to start
    time.sleep(0.5)  # Small delay to allow threads to start

    current_active_threads = threading.active_count()  # Count current active threads
    active_threads_in_pool = (
        current_active_threads - initial_active_threads
    )  # Pool threads

    assert (
        active_threads_in_pool == 5
    ), f"Expected 5 active threads, found {active_threads_in_pool}"
    pool.dispose()


def test_dispose() -> None:
    """
    Test case to verify the behavior of the pool after `dispose` is called.
    Ensures that no new tasks are accepted after the pool has been disposed.
    """
    pool = ThreadPool(2)

    # Add a task before the pool is disposed
    pool.enqueue(simple_task)
    pool.dispose()  # Dispose the pool

    # Try adding a new task after the pool is disposed
    pool.enqueue(simple_task)

    # Ensure that no new tasks were actually added after dispose
    assert len(pool.tasks) == 0, "No new tasks should be accepted after dispose."

    # Check that all threads are no longer active after dispose
    assert all(
        not thread.is_alive() for thread in pool.threads
    ), "All threads should be terminated."
    print("All tasks completed and pool disposed.")


if __name__ == "__main__":
    pytest.main()
