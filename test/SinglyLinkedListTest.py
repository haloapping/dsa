import unittest
from main.SinglyLinkedList import SinglyLinkedList


class SinglyLinkedListTest(unittest.TestCase):
    def test_insert_head_when_success(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(4):
            singly_linked_list.insert_head(i)
        self.assertEqual(singly_linked_list.insert_head(4),
                         "Data 4 inserted.")

    def test_insert_head_when_insert_one_data(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert_head(1)
        self.assertEqual(singly_linked_list.traverse(),
                         "1")

    def test_insert_head_when_insert_more_than_one_data(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(5):
            singly_linked_list.insert_head(i)
        self.assertEqual(singly_linked_list.traverse(),
                         "4->3->2->1->0")

    def test_insert_tail_when_success(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(4):
            singly_linked_list.insert_tail(i)
        self.assertEqual(singly_linked_list.insert_tail(4),
                         "Data 4 inserted.")

    def test_insert_tail_when_insert_one_data(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert_tail(1)
        self.assertEqual(singly_linked_list.traverse(),
                         "1")

    def test_insert_tail_when_insert_more_than_one_data(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert_tail(1)
        singly_linked_list.insert_tail(2)
        singly_linked_list.insert_tail(3)
        singly_linked_list.insert_tail(4)
        singly_linked_list.insert_tail(5)
        self.assertEqual(singly_linked_list.traverse(),
                         "1->2->3->4->5")

    def test_traverse_when_linked_list_is_empty(self):
        singly_linked_list = SinglyLinkedList()
        self.assertEqual(singly_linked_list.traverse(),
                         "Linked list is empty.")

    def test_insert_by_index(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(5):
            singly_linked_list.insert_by_index(i, i + 1)
        self.assertEqual(singly_linked_list.traverse(), "1->2->3->4->5")

    def test_insert_by_index_between(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert_by_index(0, 1)
        singly_linked_list.insert_by_index(1, 2)
        singly_linked_list.insert_by_index(2, 3)
        singly_linked_list.insert_by_index(3, 4)
        singly_linked_list.insert_by_index(2, 5)
        self.assertEqual(singly_linked_list.traverse(), "1->2->5->3->4")

    def test_delete_head_when_empty(self):
        singly_linked_list = SinglyLinkedList()
        self.assertEqual(singly_linked_list.delete_head(),
                         "Linked list is empty.")

    def test_delete_tail_when_empty(self):
        singly_linked_list = SinglyLinkedList()
        self.assertEqual(singly_linked_list.delete_tail(),
                         "Linked list is empty.")

    def test_delete_head_when_not_empty(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(5):
            singly_linked_list.insert_head(i)
        self.assertEqual(singly_linked_list.delete_head(),
                         "Data 4 deleted.")

    def test_delete_between(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(5):
            singly_linked_list.insert_head(i)
        self.assertEqual(singly_linked_list.delete_by_index(2),
                         "Data 2 deleted.")

    def test_delete_when_index_out_of_range(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(5):
            singly_linked_list.insert_head(i)
        self.assertEqual(singly_linked_list.delete_by_index(-1),
                         "Index out of range.")

    def test_is_empty_true(self):
        singly_linked_list = SinglyLinkedList()
        self.assertTrue(singly_linked_list.is_empty())

    def test_is_empty_false(self):
        singly_linked_list = SinglyLinkedList()
        singly_linked_list.insert_head(1)
        self.assertFalse(singly_linked_list.is_empty())
