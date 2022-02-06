from typing import Any


class QueueWithList:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.queue = []

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def is_full(self) -> bool:
        return len(self.queue) == self.max_capacity

    def enqueue(self, data: Any) -> str:
        if self.is_full():
            return "Queue is full."

        self.queue.append(data)
        return f"Enqueue {data}."

    def dequeue(self) -> str:
        return "Queue is empty." if self.is_empty() else f"Dequeue {self.queue[0]}."

    def peek_first_data(self) -> str:
        return "Queue is empty." if self.is_empty() else str(self.queue[0])

    def peek_last_data(self) -> str:
        return "Queue is empty." if self.is_empty() else str(self.queue[-1])

    def is_data_in_stack(self, data) -> str:
        return "Queue is empty." if self.is_empty() else data in self.queue

    def print(self) -> str:
        return "Queue is empty." if self.is_empty() else "<-".join(str(data) for data in self.queue)
