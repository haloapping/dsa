from typing import Any, Iterator


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class QueueWithLinkedList:
    def __init__(self, max_capacity) -> None:
        self.max_capacity = max_capacity
        self.head = None

    def __iter__(self) -> Iterator:
        """Create generator to get all value in stack.

        Yields:
            Iterator: All value in stack.
        """
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """Get number of value in stack.

        Returns:
            int: number of value in stack.
        """
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        """Check if queue is empty or not.

        Returns:
            bool: 0 is not empty and 1 is empty.
        """
        return len(self) == 0

    def is_full(self) -> bool:
        """Check id queue is full or not.

        Returns:
            bool: 0 is not full and 1 is full.
        """
        return len(self) == self.max_capacity

    def enqueue(self, data: Any) -> str:
        """Add new value from rear of queue.

        Args:
            data (Any): value added.

        Returns:
            str: message after enqueue value.
        """
        if self.is_full():
            return "Queue is full."
        elif self.is_empty():
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return f"Enqueue {data}."
        else:
            current_node = self.head
            for _ in range(len(self) - 1):
                current_node = current_node.next
            new_node = Node(data)
            current_node.next = new_node
            return f"Enqueue {data}."

    def dequeue(self) -> str:
        """Delete front value of queue.

        Returns:
            str: message after dequeue value.
        """
        if self.is_empty():
            return "Queue is empty."

        delete_node = self.head
        self.head = self.head.next

        return f"Dequeue {delete_node.data}."

    def peek_front(self) -> str:
        """Get front value.

        Returns:
            str: message after peek.
        """
        return "Queue is empty." if self.is_empty() else f"Peek {self.head.data}."

    def peek_rear(self) -> str:
        """Get rear value.

        Returns:
            str: message after peek.
        """
        current_node = self.head

        for _ in range(len(self) - 1):
            current_node = current_node.next

        return "Queue is empty." if self.is_empty() else f"Peek {current_node.data}."

    def print(self) -> str:
        return "Queue is empty." if self.is_empty() else "<-".join(str(data) for data in self)
