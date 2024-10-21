import threading
import queue
from typing import Callable, List


class ThreadPool:
    def __init__(self, num_threads: int):
        """
        Initializes the thread pool with a specified number of threads.

        Parameters:
        num_threads (int): The number of threads to be created in the pool.
        """
        self.num_threads: int = num_threads
        self.tasks: queue.Queue[Callable] = queue.Queue()
        self.threads: List[threading.Thread] = []
        self.shutdown_flag: bool = False

        self._initialize_threads()

    def _initialize_threads(self) -> None:
        """
        Initializes and starts the specified number of threads.
        Each thread will run the worker function, which continuously
        checks for tasks in the queue.
        """
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker)
            self.threads.append(thread)
            thread.start()

    def worker(self) -> None:
        """
        Worker method executed by each thread in the pool.
        This method runs in a loop, checking for tasks to execute
        from the queue. The loop continues until the shutdown flag
        is set to True.

        If a task is available, it is executed and marked as done.
        If there are no tasks available, the thread will wait briefly
        before checking again.
        """
        while not self.shutdown_flag:  # Check if the thread should shut down
            try:
                task = self.tasks.get(timeout=1)  # Wait for a task
                task()  # Execute the task
                self.tasks.task_done()  # Mark the task as done
            except queue.Empty:
                continue  # Continue if no task is found

    def enqueue(self, task: Callable) -> None:
        """
        Adds a task to the task queue. If the pool is already
        shutting down, the task will not be accepted.

        Parameters:
        task (Callable): A callable that represents the task to be executed.
        """
        if not self.shutdown_flag:
            self.tasks.put(task)  # Add task to the queue

    def dispose(self) -> None:
        """
        Gracefully shuts down the thread pool. It will wait for all
        tasks to complete and then terminate the worker threads.
        New tasks will not be accepted after this method is called.
        """
        self.shutdown_flag = True
        self.tasks.join()  # Wait for all tasks to complete
        for thread in self.threads:
            thread.join()  # Wait for all threads to terminate
