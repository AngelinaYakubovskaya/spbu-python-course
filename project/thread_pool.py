import threading
import queue


class ThreadPool:
    def __init__(self, num_threads: int):
        """
        Initializes the thread pool with a given number of threads.

        Parameters:
        num_threads (int): The number of threads in the pool.
        """
        self.num_threads = num_threads
        self.tasks = queue.Queue()  # Task queue for storing tasks
        self.threads = []  # List to store worker threads
        self.shutdown_flag = False  # Flag to signal when to shut down the pool

        self._initialize_threads()  # Initialize and start the worker threads

    def _initialize_threads(self):
        """
        Initializes and starts the specified number of threads.
        Each thread will run the worker function in a separate execution context.
        """
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker, daemon=True)
            self.threads.append(thread)
            thread.start()

    def worker(self):
        """
        Worker method executed by each thread in the pool.
        Continuously looks for tasks in the task queue and executes them. If the pool
        is in shutdown mode and no tasks are available, the thread stops execution.
        """
        while True:
            try:
                # Wait for a task from the queue, timeout after 1 second if no tasks
                task = self.tasks.get(timeout=1)
                task()  # Execute the task
                self.tasks.task_done()  # Mark the task as done
            except queue.Empty:
                if self.shutdown_flag:
                    break  # Exit the loop if the shutdown flag is set

    def enqueue(self, task: callable):
        """
        Adds a task to the task queue. Tasks are processed by available worker threads.
        If the pool is already shut down, no more tasks are accepted.

        Parameters:
        task (callable): A function representing the task to be executed by a thread.
        """
        if not self.shutdown_flag:
            self.tasks.put(task)

    def dispose(self):
        """
        Gracefully shuts down the thread pool. No new tasks will be accepted,
        but already enqueued tasks will be processed before shutting down the pool.
        This method waits for all threads to finish their tasks.
        """
        self.shutdown_flag = True
        self.tasks.join()  # Wait for all tasks to complete
        for thread in self.threads:
            thread.join()  # Wait for all threads to terminate
