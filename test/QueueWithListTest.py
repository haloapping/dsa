import unittest
from main.queue.QueueWithList import QueueWithList


class QueueWithListTest(unittest.TestCase):
    def test_enqueue_when_full(self):
        queue = QueueWithList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.enqueue(5), "Queue is full.")

    def test_enqueue_msg_when_success(self):
        queue = QueueWithList(5)
        for i in range(4):
            queue.enqueue(i)
        self.assertEqual(queue.enqueue(4), "Enqueue 4.")

    def test_dequeue_when_empty(self):
        queue = QueueWithList(5)
        self.assertEqual(queue.dequeue(), "Queue is empty.")

    def test_dequeue_msg_when_success(self):
        queue = QueueWithList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.dequeue(), "Dequeue 0.")

    def test_is_data_in_stack_when_empty(self):
        queue = QueueWithList(5)
        self.assertEqual(queue.is_data_in_stack(6), "Queue is empty.")

    def test_is_data_in_stack_not_found(self):
        queue = QueueWithList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertFalse(queue.is_data_in_stack(5))

    def test_is_data_in_stack_found(self):
        queue = QueueWithList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertTrue(queue.is_data_in_stack(4))

    def test_is_data_in_stack(self):
        queue = QueueWithList(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertFalse(queue.is_data_in_stack(6), False)

    def test_peek_first_data_when_empty(self):
        queue = QueueWithList(5)
        self.assertEqual(queue.peek_first_data(), "Queue is empty.")

    def test_peek_first_data_when_not_empty(self):
        queue = QueueWithList(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        self.assertEqual(queue.peek_first_data(), "1")

    def test_peek_last_data_when_empty(self):
        queue = QueueWithList(5)
        self.assertEqual(queue.peek_last_data(), "Queue is empty.")

    def test_peek_last_data_when_not_empty(self):
        queue = QueueWithList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.peek_last_data(), "4")

    def test_print_when_empty(self):
        queue = QueueWithList(5)
        self.assertEqual(queue.print(), "Queue is empty.")

    def test_print_when_not_empty(self):
        queue = QueueWithList(5)
        for i in range(5):
            queue.enqueue(i)
        self.assertEqual(queue.print(), "0<-1<-2<-3<-4")
