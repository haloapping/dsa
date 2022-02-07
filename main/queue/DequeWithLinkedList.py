from typing import Any, Iterator


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class DequeWithLinkedList:
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
        return self.head is None

    def is_full(self) -> bool:
        return len(self) == self.max_capacity

    def peek_front(self) -> str:
        return "Queue is empty." if self.is_empty() else str(tuple(iter(self))[0])

    def peek_rear(self) -> str:
        return "Queue is empty." if self.is_empty() else str(tuple(iter(self))[-1])

    def enqueue_front(self, data: Any) -> str:
        if self.is_full():
            return "Queue is full."
        elif self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        return f"Enqueue front {data}."

    def enqueue_rear(self, data: Any) -> str:
        if self.is_full():
            return "Queue is full."
        elif self.is_empty():
            self.head = Node(data)
        else:
            current_node = self.head
            for _ in range(len(self) - 1):
                current_node = current_node.next
            current_node.next = Node(data)
        return f"Enqueue front {data}."

    def dequeue_front(self) -> str:
        if self.is_empty():
            return "Queue is empty."

        delete_node = self.head
        self.head = self.head.next
        return f"Dequeue front {delete_node.data}."

    def dequeue_rear(self) -> str:
        if self.is_empty():
            return "Queue is empty."

        current_node = self.head
        for _ in range(len(self) - 1):
            current_node = current_node.next

        delete_node = current_node
        current_node.next = None
        return f"Dequeue rear {delete_node.data}."

    def is_data_in_queue(self, data: Any) -> str:
        if self.is_empty():
            return "Queue is empty."

        return "Found." if data in tuple(iter(self)) else "Not found."

    def print(self) -> str:
        return "Queue is empty." if self.is_empty() else "<-".join([str(data) for data in self])
