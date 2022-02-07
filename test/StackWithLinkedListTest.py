import unittest
from main.stack.StackWithLinkedList import StackWithLinkedList


class StackWithLinkedListTest(unittest.TestCase):
    def test_push_when_full(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.push(5), "Stack is full.")

    def test_push_msg_when_success(self):
        stack = StackWithLinkedList(5)
        for i in range(4):
            stack.push(i)
        self.assertEqual(stack.push(4), "Push 4.")

    def test_pop_when_empty(self):
        stack = StackWithLinkedList(5)
        self.assertEqual(stack.pop(), "Stack is empty.")

    def test_pop_msg_when_success(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.pop(), "Pop 4.")

    def test_peek_when_empty(self):
        stack = StackWithLinkedList(5)
        self.assertEqual(stack.peek(), "Stack is empty.")

    def test_peek_when_not_empty(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.peek(), "4")

    def test_print_after_peek(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        stack.peek()
        self.assertEqual(stack.print(), "4<-3<-2<-1<-0")

    def test_print_when_empty(self):
        stack = StackWithLinkedList(5)
        self.assertEqual(stack.print(), "Stack is empty.")

    def test_is_data_in_stack_when_empty(self):
        stack = StackWithLinkedList(5)
        self.assertFalse(stack.is_data_in_stack(1))

    def test_is_data_in_stack_when_not_empty(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        self.assertTrue(stack.is_data_in_stack(1))

    def test_is_data_in_stack_when_not_found(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        self.assertFalse(stack.is_data_in_stack(10))

    def test_print_when_not_empty(self):
        stack = StackWithLinkedList(5)
        for i in range(5):
            stack.push(i)
        self.assertEqual(stack.print(), "4<-3<-2<-1<-0")
