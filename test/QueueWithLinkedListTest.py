import unittest
from main.queue.QueueWithLinkedList import QueueWithLinkedList


class QueueWithLinkedListTest(unittest.TestCase):
    def test_is_full_true(self):
        queue = QueueWithLinkedList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertTrue(queue.is_full())

    def test_is_full_false(self):
        queue = QueueWithLinkedList(5)
        for i in range(4):
            queue.enqueue(i)
        self.assertFalse(queue.is_full())

    def test_is_empty_true(self):
        queue = QueueWithLinkedList(5)
        self.assertTrue(queue.is_empty())

    def test_is_empty_false(self):
        queue = QueueWithLinkedList(5)
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

    def test_peek_front_when_queue_is_empty(self):
        queue = QueueWithLinkedList(5)
        self.assertEqual(queue.peek_front(), "Queue is empty.")

    def test_peek_front_when_queue_is_not_empty(self):
        queue = QueueWithLinkedList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.peek_front(), "Peek 0.")

    def test_peek_rear_when_queue_is_empty(self):
        queue = QueueWithLinkedList(5)
        self.assertEqual(queue.peek_rear(), "Queue is empty.")

    def test_peek_rear_when_queue_is_not_empty(self):
        queue = QueueWithLinkedList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.peek_rear(), "Peek 4.")

    def test_enqueue_with_one_data(self):
        queue = QueueWithLinkedList(5)
        self.assertEqual(queue.enqueue(1), "Enqueue 1.")

    def test_dequeue_when_empty(self):
        queue = QueueWithLinkedList(5)
        self.assertEqual(queue.dequeue(), "Queue is empty.")

    def test_dequeue_when_not_empty(self):
        queue = QueueWithLinkedList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.dequeue(), "Dequeue 0.")

    def test_print_when_empty(self):
        queue = QueueWithLinkedList(5)
        self.assertEqual(queue.print(), "Queue is empty.")

    def test_print_one_data(self):
        queue = QueueWithLinkedList(5)
        queue.enqueue(1)
        self.assertEqual(queue.print(), "1")

    def test_print_more_than_one_data(self):
        queue = QueueWithLinkedList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.print(), "0->1<-2<-3<-4")

    def test_print_more_than_one_data(self):
        queue = QueueWithLinkedList(5)
        for i in range(5):
            queue.enqueue(i)

        for i in range(5):
            queue.dequeue()
        self.assertEqual(queue.print(), "Queue is empty.")
