import unittest
from main.stack.StackWithList import StackWithList


class StackWithListTest(unittest.TestCase):
    def test_push_when_not_full(self):
        stack = StackWithList(5)
        for i in range(4):
            stack.push(i)
        self.assertEqual(stack.push(4), "Push 4.")

    def test_push_when_full(self):
        stack = StackWithList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.push(5), "Stack is full.")

    def test_pop_when_empty(self):
        stack = StackWithList(5)
        self.assertEqual(stack.pop(), "Stack is empty.")

    def test_pop_when_not_empty(self):
        stack = StackWithList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), "Pop 4.")

    def test_peek_empty_stack(self):
        stack = StackWithList(5)
        self.assertEqual(stack.peek(), "Stack is empty.")

    def test_print(self):
        stack = StackWithList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.print(), [0, 1, 2, 3, 4])
