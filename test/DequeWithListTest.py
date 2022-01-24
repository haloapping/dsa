import unittest
from main.DequeWithList import DequeWithList


class DequeWithListTest(unittest.TestCase):
    def test_dequeue_front_when_queue_is_empty(self):
        deque = DequeWithList(5)
        self.assertEqual(deque.dequeue_front(), "Queue is empty.")

    def test_dequeue_front_when_after_enqueue_front(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.dequeue_front(), "Pop 4.")

    def test_dequeue_rear_when_queue_is_empty(self):
        deque = DequeWithList(5)
        self.assertEqual(deque.dequeue_rear(), "Queue is empty.")

    def test_dequeue_rear_when_after_enqueue_rear(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.dequeue_rear(), "Pop 4.")

    def test_enqueue_front_when_full(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.enqueue_front(6), "Queue is full.")

    def test_enqueue_front_when_success(self):
        deque = DequeWithList(5)
        for i in range(4):
            deque.enqueue_front(i)
        self.assertEqual(deque.enqueue_front(4), "Push 4.")

    def test_enqueue_rear_when_full(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.enqueue_rear(5), "Queue is full.")

    def test_enqueue_rear_when_success(self):
        deque = DequeWithList(5)
        for i in range(4):
            deque.enqueue_rear(i)
        self.assertEqual(deque.enqueue_rear(4), "Push 4.")

    def test_peek_front_after_enqueue_front(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.peek_front(), "4")

    def test_peek_front_after_enqueue_rear(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.peek_front(), "0")

    def test_peek_front_when_empty(self):
        deque = DequeWithList(5)
        self.assertEqual(deque.peek_front(), "Queue is empty.")

    def test_peek_rear_after_enqueue_front(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.peek_rear(), "0")

    def test_peek_rear_after_enqueue_rear(self):
        deque = DequeWithList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.peek_rear(), "4")

    def test_peek_rear_when_empty(self):
        deque = DequeWithList(5)
        self.assertEqual(deque.peek_rear(), "Queue is empty.")
