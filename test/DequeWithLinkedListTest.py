import unittest
from main.DequeWithLinkedList import DequeWithLinkedList


class DequeWithLinkedListTest(unittest.TestCase):
    def test_peek_front_when_empty(self):
        deque = DequeWithLinkedList(5)
        self.assertEqual(deque.peek_front(), "Queue is empty.")

    def test_peek_rear_when_empty(self):
        deque = DequeWithLinkedList(5)
        self.assertEqual(deque.peek_rear(), "Queue is empty.")

    def test_enqueue_front_when_full(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.enqueue_front(5), "Queue is full.")

    def test_enqueue_front_when_success(self):
        deque = DequeWithLinkedList(5)
        for i in range(4):
            deque.enqueue_front(i)
        self.assertEqual(deque.enqueue_front(3), "Enqueue front 3.")

    def test_enqueue_rear_when_full(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.enqueue_rear(5), "Queue is full.")

    def test_enqueue_rear_when_success(self):
        deque = DequeWithLinkedList(5)
        for i in range(4):
            deque.enqueue_rear(i)
        self.assertEqual(deque.enqueue_rear(3), "Enqueue front 3.")

    def test_dequeue_front_when_empty(self):
        deque = DequeWithLinkedList(5)
        self.assertEqual(deque.dequeue_front(), "Queue is empty.")

    def test_dequeue_front_after_enqueue_front(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.dequeue_front(), "Dequeue front 4.")

    def test_dequeue_front_after_enqueue_rear(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.dequeue_front(), "Dequeue front 0.")

    def test_dequeue_rear_when_empty(self):
        deque = DequeWithLinkedList(5)
        self.assertEqual(deque.dequeue_rear(), "Queue is empty.")

    def test_dequeue_rear_after_enqueue_front(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.dequeue_rear(), "Dequeue rear 0.")

    def test_dequeue_rear_after_enqueue_rear(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_rear(i)
        self.assertEqual(deque.dequeue_rear(), "Dequeue rear 4.")

    def test_is_data_in_queue_when_empty(self):
        deque = DequeWithLinkedList(5)
        self.assertEqual(deque.is_data_in_queue(1), "Queue is empty.")

    def test_is_data_in_queue_when_not_found(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.is_data_in_queue(5), "Not found.")

    def test_is_data_in_queue_when_found(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.is_data_in_queue(3), "Found.")

    def test_print_when_empty(self):
        deque = DequeWithLinkedList(5)
        self.assertEqual(deque.print(), "Queue is empty.")

    def test_print_after_enqueue_front(self):
        deque = DequeWithLinkedList(5)
        for i in range(5):
            deque.enqueue_front(i)
        self.assertEqual(deque.print(), "4<-3<-2<-1<-0")
