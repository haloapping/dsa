import random
import unittest
from main.BubbleSort import BubbleSort

unsorted_items = [random.randint(-1000, 1_000) for _ in range(1_000)]
asc_sorted_items = sorted(unsorted_items)
desc_sorted_items = sorted(unsorted_items, reverse=True)
sorted_items = list(range(10_000))


class BubbleSortTest(unittest.TestCase, unittest.TestLoader):
    def test_is_empty(self):
        bubble_sort = BubbleSort([])
        self.assertEqual(bubble_sort.print(), "List of data is empty.")

    def test_print_before_sort(self):
        bubble_sort = BubbleSort(unsorted_items)
        self.assertEqual(bubble_sort.print(),
                         str(unsorted_items))

    def test_sort_when_mode_not_found(self):
        bubble_sort = BubbleSort(unsorted_items)
        self.assertEqual(bubble_sort.sort("random"), "Mode random not found.")

    def test_print_after_sort_ascending(self):
        bubble_sort = BubbleSort(unsorted_items)
        bubble_sort.sort("asc")
        self.assertEqual(bubble_sort.print(), str(asc_sorted_items))

    def test_print_after_sort_descending(self):
        bubble_sort = BubbleSort(unsorted_items)
        bubble_sort.sort("desc")
        self.assertEqual(bubble_sort.print(), str(desc_sorted_items))

    def test_swap_false(self):
        bubble_sort = BubbleSort(list(range(10)))
        bubble_sort.sort("asc")
        self.assertFalse(bubble_sort.swapped)

    def test_swap_true(self):
        bubble_sort = BubbleSort(unsorted_items)
        bubble_sort.sort("asc")
        self.assertTrue(bubble_sort.swapped)
