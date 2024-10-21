import threading
import queue
from typing import Callable, List


class ThreadPool:
    def __init__(self, num_threads: int):
        """
        Initializes the thread pool with a given number of threads.

        Parameters:
        num_threads (int): The number of threads in the pool.
        """
        self.num_threads: int = num_threads
        self.tasks: queue.Queue[Callable] = queue.Queue()
        self.threads: List[threading.Thread] = []
        self.shutdown_flag: bool = False

        self._initialize_threads()

    def _initialize_threads(self) -> None:
        """Initializes and starts the specified number of threads."""
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker)
            self.threads.append(thread)
            thread.start()

    def worker(self) -> None:
        """Worker method executed by each thread in the pool."""
        while True:
            try:
                task = self.tasks.get(timeout=1)  # Wait for a task
                if task is None:  # Shutdown signal
                    break
                task()  # Execute the task
                self.tasks.task_done()  # Mark the task as done
            except queue.Empty:
                if self.shutdown_flag:
                    break  # Exit the loop if shutdown flag is set

    def enqueue(self, task: Callable) -> None:
        """Adds a task to the task queue."""
        if not self.shutdown_flag:
            self.tasks.put(task)  # Add task to the queue

    def dispose(self) -> None:
        """Gracefully shuts down the thread pool."""
        self.shutdown_flag = True
        for _ in range(self.num_threads):
            self.tasks.put(None)  # Send shutdown signal to each thread
        self.tasks.join()  # Wait for all tasks to complete
        for thread in self.threads:
            thread.join()  # Wait for all threads to terminate
