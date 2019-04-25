import unittest
from .arrays import *

class ArrayProuctTest(unittest.TestCase):
    def test_gets_product_of_items_excluding_item_at_index(self):
      number_lists = [5, 10, 1]
      self.assertEqual(multiply_array_items(number_lists), [10, 5, 50])

    def test_handles_arrays_with_zero(self):
      number_lists_with_zero = [5, 10, 1, 0]
      self.assertEqual(multiply_array_items(number_lists_with_zero), [0, 0, 0, 50])