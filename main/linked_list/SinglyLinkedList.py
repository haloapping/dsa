from typing import Any


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> Any:
        current_node = self.head
        while current_node:
            yield current_node.data
            current_node = current_node.next

    def __len__(self) -> int:
        """Get number of node from linked list."""
        return len(tuple(iter(self)))

    def insert_head(self, data: Any) -> str:
        return self.insert_by_index(0, data)

    def insert_tail(self, data: Any) -> str:
        return self.insert_by_index(len(self), data)

    def delete_head(self) -> str:
        return self.delete_by_index(0)

    def delete_tail(self) -> str:
        return self.delete_by_index(len(self) - 1)

    def insert_by_index(self, index: int, data: Any) -> str:
        if not 0 <= index <= len(self):
            return "Index out of range."

        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node
        return f"Data {data} inserted."

    def delete_by_index(self, index: int) -> str:
        if self.is_empty():
            return "Linked list is empty."
        elif not 0 <= index <= len(self) - 1:
            return "Index out of range."
        elif index == 0:
            delete_node = self.head.data
            self.head = self.head.next
            return f"Data {delete_node} deleted."
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            delete_node = current_node.next
            current_node.next = current_node.next.next
            return f"Data {delete_node.data} deleted."

    def is_empty(self) -> bool:
        return len(self) == 0

    def traverse(self) -> str:
        return "Linked list is empty." if self.is_empty() else "->".join([str(data) for data in self])
