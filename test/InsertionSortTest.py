import random
import unittest
from main.sort.InsertionSort import InsertionSort

value_range = 10
unsorted_items = [random.randint(-value_range, value_range)
                  for _ in range(value_range)]
asc_sorted_items = sorted(unsorted_items)
desc_sorted_items = sorted(unsorted_items, reverse=True)
sorted_items = list(range(value_range))


class InsertionSortTest(unittest.TestCase):
    def test_is_empty_list(self):
        insertion_sort = InsertionSort([])
        self.assertTrue(insertion_sort.is_empty())

    def test_sort_when_mode_not_available(self):
        insertion_sort = InsertionSort(unsorted_items)
        self.assertEqual(insertion_sort.sort("random"),
                         "Mode random is not available.")

    def test_sort_asc_when_list_empty(self):
        insertion_sort = InsertionSort([])
        self.assertEqual(insertion_sort.sort("asc"), "List is empty.")

    def test_sort_asc_when_list_not_empty(self):
        insertion_sort = InsertionSort(unsorted_items)
        self.assertEqual(insertion_sort.sort("asc"), str(asc_sorted_items))

    def test_sort_desc_when_list_empty(self):
        insertion_sort = InsertionSort([])
        self.assertEqual(insertion_sort.sort("desc"), "List is empty.")

    def test_sort_desc_when_list_not_empty(self):
        insertion_sort = InsertionSort(unsorted_items)
        self.assertEqual(insertion_sort.sort("desc"), str(desc_sorted_items))

    def test_print_when_empty_list(self):
        insertion_sort = InsertionSort([])
        self.assertEqual(insertion_sort.print(), "List is empty.")

    def test_print_when_not_empty_list(self):
        insertion_sort = InsertionSort(unsorted_items)
        insertion_sort.sort("asc")
        self.assertEqual(insertion_sort.print(), str(asc_sorted_items))
