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
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        return len(self) == self.max_capacity

    def enqueue(self, data: Any) -> str:
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
        if self.is_empty():
            return "Queue is empty."

        delete_node = self.head
        self.head = self.head.next

        return f"Dequeue {delete_node.data}."

    def peek(self) -> str:
        return "Queue is empty." if self.is_empty() else f"Peek {self.head.data}."

    def print(self) -> str:
        return "Queue is empty." if self.is_empty() else "<-".join(str(data) for data in self)
