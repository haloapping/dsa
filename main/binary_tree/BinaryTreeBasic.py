from typing import Any


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTreeBasic:
    def __init__(self) -> None:
        self.root = None

    def is_empty(self, root: Node) -> bool:
        return root.data is None

    def get_min_value(self, root: Node) -> str:
        if self.is_empty(root):
            return "Tree is empty."

        node = root
        prev_node = None
        while node:
            prev_node = node
            node = node.left

        return f"Max value is {prev_node.data}"

    def get_max_value(self, root: Node) -> str:
        if self.is_empty(root):
            return "Tree is empty."

        node = root
        prev_node = None
        while node:
            prev_node = node
            node = node.right

        return f"Max value is {prev_node.data}"

    def preorder(self, root: Node) -> Any:
        if root:
            self.preorder(root.left)
            print(f"{root.data}", end="")
            self.preorder(root.right)

    def inorder(self, root: Node) -> Any:
        if root:
            self.preorder(root.left)
            print(f"{root.data}", end="")
            self.preorder(root.right)

    def postorder(self, root: Node) -> Any:
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            print(f"{root.data}", end="")

    def display(self, mode: str, root: Node) -> Any:
        if self.is_empty(root):
            return "Tree is empty."
        elif mode == "pre":
            self.preorder(root)
        elif mode == "post":
            self.postorder(root)
        elif mode == "in":
            self.inorder(root)
        else:
            return f"{mode.capitalize()} not found. Use pre, in, post keyword."
