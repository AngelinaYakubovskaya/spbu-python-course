import threading
import time
import pytest
from project.thread_pool import ThreadPool


def simple_task() -> None:
    """
    Example task for the thread pool.
    Simulates a task by printing the thread name and sleeping for 1 second.
    """
    print(f"Task executed by {threading.current_thread().name}")
    time.sleep(1)


def test_enqueue_and_task_execution() -> None:
    """
    Test case to verify that tasks are properly enqueued and executed by the pool.
    """
    pool = ThreadPool(3)

    tasks_completed = []

    def task() -> None:
        tasks_completed.append(threading.current_thread().name)

    # Enqueue 5 tasks
    for _ in range(5):
        pool.enqueue(task)

    pool.dispose()

    # Check that all tasks were completed
    assert len(tasks_completed) == 5, "Not all tasks were completed."
    print(f"Tasks completed: {tasks_completed}")


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

    # Check that no new tasks are accepted after dispose
    assert len(pool.tasks) == 2, "No new tasks should be accepted after dispose."
    print("Pool has been disposed, no more tasks should be accepted.")


def test_graceful_shutdown() -> None:
    """
    Test case to ensure that the pool completes all tasks before shutting down.
    """
    pool = ThreadPool(2)

    tasks_completed = []

    def task() -> None:
        tasks_completed.append(threading.current_thread().name)
        time.sleep(0.5)

    # Enqueue 3 tasks
    for _ in range(3):
        pool.enqueue(task)

    pool.dispose()  # Shut down the pool after all tasks are enqueued

    # Check that all tasks were completed before shutdown
    assert len(tasks_completed) == 3, "Not all tasks were completed before shutdown."
    print(f"Tasks completed before shutdown: {tasks_completed}")


if __name__ == "__main__":
    pytest.main()
