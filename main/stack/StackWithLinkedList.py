from typing import Any, Iterator


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None


class StackWithLinkedList:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.head = None

    def __iter__(self) -> Iterator:
        """Get each data by sequential."""
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """Get number of node."""
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        return self.head is None

    def is_full(self) -> bool:
        return len(tuple(iter(self))) == self.max_capacity

    def push(self, data: Any) -> str:
        """Push data on top stack."""
        if self.is_full():
            return "Stack is full."
        elif self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        return f"Push {data}."

    def pop(self) -> str:
        """Remove data from top stack."""
        if self.is_empty():
            return "Stack is empty."

        current_node = self.head
        for _ in range(len(self) - 2):
            current_node = current_node.next

        delete_data = self.head.data
        self.head = current_node
        current_node.next = None
        return f"Pop {delete_data}."

    def peek(self) -> str:
        """Check value of data from top stack."""
        return "Stack is empty." if self.is_empty() else str(self.head.data)

    def is_data_in_stack(self, data: Any) -> bool:
        """Check data exist in stack."""
        return data in list(self)

    def print(self) -> str:
        return "Stack is empty." if self.is_empty() else "<-".join([str(data) for data in self])
