from typing import Any


class QueueWithList:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.queue = []

    def is_empty(self) -> bool:
        """Check if queue is empty or not.

        Returns:
            bool: 0 is not empty and 1 is empty.
        """
        return len(self.queue) == 0

    def is_full(self) -> bool:
        """Check id queue is full or not.

        Returns:
            bool: 0 is not full and 1 is full.
        """
        return len(self.queue) == self.max_capacity

    def enqueue(self, data: Any) -> str:
        """Add new value from rear of queue.

        Args:
            data (Any): value added.

        Returns:
            str: message after enqueue value.
        """
        if self.is_full():
            return "Queue is full."

        self.queue.append(data)
        return f"Enqueue {data}."

    def dequeue(self) -> str:
        """Delete front value of queue.

        Returns:
            str: message after dequeue value.
        """
        return "Queue is empty." if self.is_empty() else f"Dequeue {self.queue[0]}."

    def peek_front(self) -> str:
        """Get front value.

        Returns:
            str: message after peek.
        """
        return "Queue is empty." if self.is_empty() else str(self.queue[0])

    def peek_rear(self) -> str:
        """Get rear value.

        Returns:
            str: message after peek
        """
        return "Queue is empty." if self.is_empty() else str(self.queue[-1])

    def is_data_in_stack(self, data: Any) -> str:
        """Check is data exist in queue.

        Args:
            data (Any): searched value.

        Returns:
            str: message after check data.
        """
        return "Queue is empty." if self.is_empty() else data in self.queue

    def print(self) -> str:
        """Get all data in string format.

        Returns:
            str: All data in string format.
        """
        return "Queue is empty." if self.is_empty() else "<-".join(str(data) for data in self.queue)
