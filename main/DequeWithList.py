from collections import deque
from typing import Any


class DequeWithList:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.deque = []

    def is_empty(self) -> bool:
        return len(self.deque) == 0

    def is_full(self) -> bool:
        return len(self.deque) == self.max_capacity

    def enqueue_front(self, data: Any) -> str:
        if self.is_full():
            return "Queue is full."

        self.deque.insert(0, data)
        return f"Push {data}."

    def enqueue_rear(self, data: Any) -> str:
        if self.is_full():
            return "Queue is full."

        self.deque.append(data)
        return f"Push {data}."

    def dequeue_front(self) -> str:
        if self.is_empty():
            return "Queue is empty."

        data_pop = self.deque[0]
        self.deque.pop(0)
        return f"Pop {data_pop}."

    def dequeue_rear(self) -> str:
        if self.is_empty():
            return "Queue is empty."

        data_pop = self.deque[-1]
        self.deque.pop(-1)
        return f"Pop {data_pop}."

    def peek_front(self) -> str:
        return "Queue is empty." if self.is_empty() else str(self.deque[0])

    def peek_rear(self) -> str:
        return "Queue is empty." if self.is_empty() else str(self.deque[-1])
