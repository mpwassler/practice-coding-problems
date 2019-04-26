import unittest
from .strings import *

class AnagramsTest(unittest.TestCase):
    def test_finds_anagrams_index(self):
      w = "ab"
      s = "abxaba"
      self.assertEqual(find_anagram_indices(w,s), [0,3,4])