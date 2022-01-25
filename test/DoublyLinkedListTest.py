import unittest
from main.linked_list.DoublyLinkedList import DoublyLinkedList


class DoublyLinkedListTest(unittest.TestCase):
    def test_linked_list_is_empty(self):
        doubly_linked_list = DoublyLinkedList()
        self.assertTrue(doubly_linked_list.is_empty())

    # insert
    def test_print_after_insert_head_when_linked_list_is_empty(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_head(1)
        self.assertEqual(doubly_linked_list.print(), "1")

    def test_msg_inserted_when_inserted_head(self):
        doubly_linked_list = DoublyLinkedList()
        self.assertEqual(doubly_linked_list.insert_head(1), "Inserted 1.")

    def test_print_after_insert_head_when_linked_list_in_not_empty(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_head(i)
        self.assertEqual(doubly_linked_list.print(), "4<-3<-2<-1<-0")

    def test_print_after_insert_head_and_insert_by_index(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_head(i)
        doubly_linked_list.insert_by_index(2, 5)
        self.assertEqual(doubly_linked_list.print(), "4<-3<-5<-2<-1<-0")

    def test_print_after_insert_tail_when_linked_list_is_empty(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_tail(1)
        self.assertEqual(doubly_linked_list.print(), "1")

    def test_msg_inserted_when_inserted_tail(self):
        doubly_linked_list = DoublyLinkedList()
        self.assertEqual(doubly_linked_list.insert_tail(1), "Inserted 1.")

    def test_print_after_insert_tail_when_linked_list_not_is_empty(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_tail(i)
        self.assertEqual(doubly_linked_list.print(), "0<-1<-2<-3<-4")

    def test_print_after_insert_tail_and_insert_by_index(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_tail(i)
        doubly_linked_list.insert_by_index(2, 5)
        self.assertEqual(doubly_linked_list.print(), "0<-1<-5<-2<-3<-4")

    def test_negative_index_when_insert_by_index(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_tail(i)
        self.assertEqual(
            doubly_linked_list.insert_by_index(-1, 5), "Index out of range.")

    def test_index_greater_than_length_of_linked_list_when_insert_by_index(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_tail(i)
        self.assertEqual(
            doubly_linked_list.insert_by_index(6, 5), "Index out of range.")

    # delete
    def test_delete_head_when_lisked_list_is_empty(self):
        doubly_linked_list = DoublyLinkedList()
        self.assertEqual(doubly_linked_list.delete_head(),
                         "Linked list is empty.")

    def test_delete_head_when_num_node_is_1(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_head(1)
        self.assertEqual(doubly_linked_list.delete_head(), "Deleted 1")

    def test_print_delete_head_when_num_node_is_1(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_head(1)
        doubly_linked_list.delete_head()
        self.assertEqual(doubly_linked_list.print(), "Linked list is empty.")

    def test_delete_head_when_num_node_is_1(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_tail(1)
        self.assertEqual(doubly_linked_list.delete_tail(), "Deleted 1")

    def test_print_delete_tail_when_num_node_is_1(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_tail(1)
        doubly_linked_list.delete_tail()
        self.assertEqual(doubly_linked_list.print(), "Linked list is empty.")

    def test_msg_delete_tail_when_num_node_more_than_1(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_tail(i)
        self.assertEqual(doubly_linked_list.delete_tail(), "Deleted 4")

    def test_print_after_insert_head_and_delete_by_index(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_head(i)
        doubly_linked_list.delete_by_index(2)
        self.assertEqual(doubly_linked_list.print(), "4<-3<-1<-0")

    def test_print_after_insert_tail_and_delete_by_index(self):
        doubly_linked_list = DoublyLinkedList()
        for i in range(5):
            doubly_linked_list.insert_tail(i)
        doubly_linked_list.delete_by_index(4)
        self.assertEqual(doubly_linked_list.print(), "0<-1<-2<-3")

    def test_delete_tail_when_lisked_list_is_empty(self):
        doubly_linked_list = DoublyLinkedList()
        self.assertEqual(doubly_linked_list.delete_tail(),
                         "Linked list is empty.")
