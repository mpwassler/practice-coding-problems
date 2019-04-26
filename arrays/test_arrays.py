import unittest
from .arrays import *

class ArrayProuctTest(unittest.TestCase):
    def test_gets_product_of_items_excluding_item_at_index(self):
      number_lists = [5, 10, 1]
      self.assertEqual(multiply_array_items(number_lists), [10, 5, 50])

    def test_handles_arrays_with_zero(self):
      number_lists_with_zero = [5, 10, 1, 0]
      self.assertEqual(multiply_array_items(number_lists_with_zero), [0, 0, 0, 50])

class ArrayMinSortRangeTest(unittest.TestCase):
    def test_gets_min_sort_range(self):
      number_lists = [3,7,5,6,9]
      self.assertEqual(window(number_lists), (1, 3))

    def test_handles_whole_list(self):
      number_lists = [3,7,5,6,9,1]
      self.assertEqual(window(number_lists), (0, 5))

class MaxSubArraySum(unittest.TestCase):
    def test_gets_max_sub_array_sum(self):
      number_lists = [34, -50, 42, 14, -5, 86]
      self.assertEqual(sub_array_sum(number_lists), 137)

    def test_can_take_none(self):
      number_lists = [-5, -1, -8, -9]
      self.assertEqual(sub_array_sum(number_lists), 0)

class SmallerElementsToRightTest(unittest.TestCase):
    def test_finds_smaller_elements_to_right(self):
      number_list = [3,4,9,6,1]
      self.assertEqual(smaller_counts(number_list), [1,1,2,1,0])