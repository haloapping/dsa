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
        """Check if binary tree is empty or not.

        Returns:
            bool: 0 is not empty and 1 is empty.
        """
        return root.data is None

    def get_min_value(self, root: Node) -> str:
        """Get minimal value in binary tree.

        Args:
            root (Node): root node in binary tree.

        Returns:
            str: return minimal value else message empty tree.
        """
        if self.is_empty(root):
            return "Tree is empty."

        node = root
        prev_node = None
        while node:
            prev_node = node
            node = node.left

        return f"Max value is {prev_node.data}"

    def get_max_value(self, root: Node) -> str:
        """Get maximal value in binary tree.

        Args:
            root (Node): root node in binary tree.

        Returns:
            str: return maximal value else message empty tree.
        """
        if self.is_empty(root):
            return "Tree is empty."

        node = root
        prev_node = None
        while node:
            prev_node = node
            node = node.right

        return f"Max value is {prev_node.data}"

    def preorder(self, root: Node) -> Any:
        """Get data from root->left->right.

        Args:
            root (Node): data, left node, and right node.

        Returns:
            Any: print data in preorder.
        """
        if root:
            print(f"{root.data}", end="")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root: Node) -> Any:
        """Get data from left->root->right.

        Args:
            root (Node): data, left node, and right node.

        Returns:
            Any: print data in inorder.
        """
        if root:
            self.inorder(root.left)
            print(f"{root.data}", end="")
            self.inorder(root.right)

    def postorder(self, root: Node) -> Any:
        """Get data from left->right->root.

        Args:
            root (Node): data, left node, and right node.

        Returns:
            Any: print data in postorder.
        """
        if root:
            self.preorder(root.left)
            self.preorder(root.right)
            print(f"{root.data}", end="")

    def display(self, mode: str, root: Node) -> Any:
        """Display all value in string format.

        Args:
            mode (str): ascending or descending.
            root (Node): root node of bianry tree.

        Returns:
            str: if tree is empty return message else all data in format string.
        """
        if self.is_empty(root):
            return "Tree is empty."
        elif mode == "pre":
            self.preorder(root)
        elif mode == "post":
            self.postorder(root)
        elif mode == "in":
            self.inorder(root)
        else:
            return f"{mode.capitalize()} not found. Use pre, in, or post keyword."
