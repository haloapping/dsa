from typing import Any


class StackWithList:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.stack = []

    def is_empty(self) -> bool:
        """Check if the stack is empty.

        Returns:
            bool: 0 is not empty and 1 is empty.
        """
        return len(self.stack) == 0

    def is_full(self) -> bool:
        """Check if the stack is full.

        Returns:
            bool: 0 is full and 1 is full.
        """
        return len(self.stack) == self.max_capacity

    def push(self, data: Any) -> str:
        """Add new value on top stack.

        Args:
            data (Any): entered value.

        Returns:
            str: message after enter value.
        """
        if not self.is_full():
            self.stack.append(data)
            return f"Push {data}."

        return "Stack is full."

    def pop(self) -> str:
        """Delete value from top stack.

        Returns:
            str: Message after delete value.
        """
        if self.is_empty():
            return "Stack is empty."

        pop_data = self.stack[-1]
        self.stack.pop()
        return f"Pop {pop_data}."

    def peek(self) -> str:
        """Check top value in stack.

        Returns:
            str: Message after check top value.
        """
        return "Stack is empty." if self.is_empty() else str(self.stack[-1])

    def print(self) -> list:
        """Get all value in stack.

        Returns:
            list: Get all value in list format.
        """
        return self.stack
