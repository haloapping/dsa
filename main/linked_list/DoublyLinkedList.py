from typing import Any


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

current_node = node_1.next
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> Any:
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        return self.head is None

    def insert_head(self, data):
        return self.insert_by_index(0, data)

    def insert_tail(self, data):
        return self.insert_by_index(len(self), data)

    def insert_by_index(self, index, data):
        if not 0 <= index <= len(self):
            return "Index out of range."

        if self.is_empty():
            self.head = Node(data)
        elif index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node = Node(data)
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next = new_node
            current_node.next.prev = new_node

        return f"Inserted {data}."

    def delete_head(self):
        return self.delete_by_index(0)

    def delete_tail(self):
        return self.delete_by_index(len(self) - 1)

    def delete_by_index(self, index):
        if self.is_empty():
            return "Linked list is empty."

        if len(self) == 1:
            delete_data = self.head.data
            self.head = None
            return f"Deleted {delete_data}"
        elif index == len(self) - 1:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            delete_data = current_node.next.data
            current_node.prev = None
            current_node.next = None
            return f"Deleted {delete_data}"
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            delete_data = current_node.next.data
            current_node.next = current_node.next.next
            current_node.next.next.prev = current_node
            print(current_node.next.data)

        return f"Deleted {delete_data}"

    def print(self):
        return "Linked list is empty." if self.is_empty() else "<-".join([str(data) for data in self])
