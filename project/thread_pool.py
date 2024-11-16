import threading
from typing import Callable, List, Optional


class ThreadPool:
    def __init__(self, num_threads: int):
        """
        Initializes the thread pool with a given number of threads.
        """
        self.num_threads: int = num_threads
        self.tasks: List[Optional[Callable]] = []  # Список задач
        self.threads: List[threading.Thread] = []  # Список потоков
        self.condition = (
            threading.Condition()
        )  # Условие для синхронизации доступа к задачам
        self.is_shutdown = False  # Флаг завершения работы пула

        self._initialize_threads()  # Инициализация и запуск потоков

    def _initialize_threads(self) -> None:
        """
        Initializes and starts the specified number of threads.
        Each thread will run the worker function in a separate execution context.
        """
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.worker, daemon=True)
            self.threads.append(thread)
            thread.start()

    def worker(self) -> None:
        """
        Worker method executed by each thread in the pool.
        Continuously looks for tasks in the task list and executes them.
        If the pool receives a `None` task, the thread stops execution.
        """
        while True:
            with self.condition:
                while not self.tasks:
                    self.condition.wait()  # Ждём, пока не появятся задачи

                task = self.tasks.pop(0)  # Извлекаем задачу из очереди

            if task is None:  # Специальная задача, которая завершает поток
                break

            task()  # Выполняем задачу

    def enqueue(self, task: Callable) -> None:
        """
        Adds a task to the task list. Tasks are processed by available worker threads.
        Prevents adding new tasks if the pool is in the shutdown state.
        """
        with self.condition:
            if self.is_shutdown:
                return  # Не разрешаем добавлять новые задачи после завершения пула
            self.tasks.append(task)  # Добавляем задачу в список
            self.condition.notify()  # Уведомляем один из потоков о новой задаче

    def dispose(self) -> None:
        """
        Gracefully shuts down the thread pool. No new tasks will be accepted,
        and special `None` tasks will be enqueued to stop the worker threads.
        """
        with self.condition:
            self.is_shutdown = True  # Устанавливаем флаг завершения
            # Добавляем по одному `None` на каждый поток, чтобы завершить его
            for _ in range(self.num_threads):
                self.tasks.append(None)
            self.condition.notify_all()  # Уведомляем все потоки

        for thread in self.threads:
            thread.join()  # Ожидаем завершения всех потоков
