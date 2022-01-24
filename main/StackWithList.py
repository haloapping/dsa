from typing import Any


class StackWithList:
    def __init__(self, max_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def is_full(self) -> bool:
        return len(self.stack) == self.max_capacity

    def push(self, data: Any) -> str:
        if not self.is_full():
            self.stack.append(data)
            return f"Push {data}."

        return "Stack is full."

    def pop(self) -> str:
        if self.is_empty():
            return "Stack is empty."

        pop_data = self.stack[-1]
        self.stack.pop()
        return f"Pop {pop_data}."

    def peek(self) -> str:
        return "Stack is empty." if self.is_empty() else str(self.stack[-1])

    def print(self) -> list:
        return self.stack
