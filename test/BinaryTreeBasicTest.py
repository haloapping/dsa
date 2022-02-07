import unittest
from main.binary_tree.BinaryTreeBasic import Node, BinaryTreeBasic


class BinaryTreeTest(unittest.TestCase):
    def test_tree_is_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertTrue(binary_tree_basic.is_empty(root))

    # Min value
    def test_get_min_value_when_root_is_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertEqual(binary_tree_basic.get_min_value(
            root), "Tree is empty.")

    def test_get_min_value_when_root_is_not_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node(1)
        self.assertEqual(binary_tree_basic.get_min_value(
            root), "Max value is 1")

    def test_get_min_value_when_data_more_than_one(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        root.right = Node(4)
        root.right.right = Node(5)
        self.assertEqual(binary_tree_basic.get_min_value(
            root), "Max value is 1")

    # Max value
    def test_get_max_value_when_root_is_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertEqual(binary_tree_basic.get_max_value(
            root), "Tree is empty.")

    def test_get_max_value_when_root_is_not_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node(1)
        self.assertEqual(binary_tree_basic.get_max_value(
            root), "Max value is 1")

    def test_get_max_value_when_data_more_than_one(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        root.right = Node(4)
        root.right.right = Node(5)
        self.assertEqual(binary_tree_basic.get_max_value(
            root), "Max value is 5")

    # Display
    def test_display_preorder_when_root_is_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertEqual(binary_tree_basic.display(
            "pre", root), "Tree is empty.")

    def test_display_preorder_when_root_is_not_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertEqual(binary_tree_basic.display(
            "pre", root), "Tree is empty.")

    def test_display_inorder_when_root_is_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertEqual(binary_tree_basic.display(
            "in", root), "Tree is empty.")

    def test_display_postorder_when_root_is_empty(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node()
        self.assertEqual(binary_tree_basic.display(
            "post", root), "Tree is empty.")

    def test_display_when_mode_not_found(self):
        binary_tree_basic = BinaryTreeBasic()
        root = Node(3)
        root.left = Node(2)
        root.left.left = Node(1)
        root.right = Node(4)
        root.right.right = Node(5)
        self.assertEqual(binary_tree_basic.display(
            "random", root), "Random not found. Use pre, in, post keyword.")
