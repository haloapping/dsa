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
        """Check if stack is empty or not.

        Returns:
            bool: 0 is not empty and 1 is empty.
        """
        return self.head is None

    def is_full(self) -> bool:
        """Check if stack is full or not.

        Returns:
            bool: 0 is not full and is full.
        """
        return len(tuple(iter(self))) == self.max_capacity

    def push(self, data: Any) -> str:
        """Add new value on top stack.

        Args:
            data (Any): entered value.

        Returns:
            str: message after enter value.
        """
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
        """Delete value from top stack.

        Returns:
            str: Message after delete value.
        """
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
        """Check top value in stack.

        Returns:
            str: Message after check top value.
        """
        return "Stack is empty." if self.is_empty() else str(self.head.data)

    def is_data_in_stack(self, data: Any) -> bool:
        """Check if certain data is exist in stack.

        Args:
            data (Any): searched value.

        Returns:
            bool: 0 is not found and 1 is found.
        """
        return data in list(self)

    def print(self) -> str:
        """Get all value in stack in string format

        Returns:
            str: all value in string format.
        """
        return "Stack is empty." if self.is_empty() else "<-".join([str(data) for data in self])
