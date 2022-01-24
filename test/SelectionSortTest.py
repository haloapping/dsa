import random
import unittest
from main.SelectionSort import SelectionSort

value_range = 10
unsorted_items = [random.randint(-value_range, value_range)
                  for _ in range(value_range)]
asc_sorted_items = sorted(unsorted_items)
desc_sorted_items = sorted(unsorted_items, reverse=True)
sorted_items = list(range(value_range))


class SelectionSortTest(unittest.TestCase):
    def test_is_empty_list(self):
        selection_sort = SelectionSort([])
        self.assertTrue(selection_sort.is_empty())

    def test_sort_when_mode_not_available(self):
        selection_sort = SelectionSort(unsorted_items)
        self.assertEqual(selection_sort.sort(
            "random"), "Mode random not available.")

    def test_sort_when_list_is_empty(self):
        selection_sort = SelectionSort([])
        self.assertEqual(selection_sort.sort("asc"), "List is empty.")

    def test_sort_ascending_when_list_empty(self):
        selection_sort = SelectionSort([])
        self.assertEqual(selection_sort.sort("asc"), "List is empty.")

    def test_sort_ascending_when_not_list_empty(self):
        selection_sort = SelectionSort(unsorted_items)
        self.assertEqual(selection_sort.sort("asc"), str(asc_sorted_items))

    def test_sort_descending_when_list_empty(self):
        selection_sort = SelectionSort([])
        self.assertEqual(selection_sort.sort("desc"), "List is empty.")

    def test_sort_descending_when_not_list_empty(self):
        selection_sort = SelectionSort(unsorted_items)
        self.assertEqual(selection_sort.sort("desc"), str(desc_sorted_items))

    def test_print_is_empty(self):
        selection_sort = SelectionSort([])
        self.assertEqual(selection_sort.print(), "List is empty.")

    def test_print_after_sort_asc(self):
        selection_sort = SelectionSort(unsorted_items)
        selection_sort.sort("asc")
        self.assertEqual(selection_sort.print(), str(asc_sorted_items))

    def test_print_after_sort_desc(self):
        selection_sort = SelectionSort(unsorted_items)
        selection_sort.sort("desc")
        self.assertEqual(selection_sort.print(), str(desc_sorted_items))
