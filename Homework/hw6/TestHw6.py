import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted

class Test_SortHalfSorted(unittest.TestCase):
   def test_halfsorted_bubble(self):
      "Tests bubble sort algorithm"
      # use sort_halfsorted(L, bubble) to test
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(9, 10):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                              # Generate a half-sorted list
                              L1, idx = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                              # Make a deep-copy of that list using slicing
                              L2 = L1[:]
                              # Sort the original list using e.g. `sort_halfsorted(L, bubble)`
                              sort_halfsorted(L1, bubble)
                              # Test that the original list is now sorted
                              self.assertTrue(is_sorted(L1))
                              # Test that the original list and the deep copy have the same elements
                              self.assertCountEqual(L1, L2)

   def test_halfsorted_selection(self):
      "Tests selection sort algorithm"
      # use sort_halfsorted(L, selection) to test
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                           # Generate a half-sorted list
                           L1, idx = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                           # Make a deep-copy of that list using slicing
                           L2 = L1[:]
                           # Sort the original list using e.g. `sort_halfsorted(L, bubble)`
                           sort_halfsorted(L1, selection)
                           # Test that the original list is now sorted
                           self.assertTrue(is_sorted(L1))
                           # Test that the original list and the deep copy have the same elements
                           self.assertCountEqual(L1, L2)

   def test_halfsorted_insertion(self):
      "Tests insertion sort algorithm"
      # use sort_halfsorted(L, insertion) to test
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                           # Generate a half-sorted list
                           L1, idx = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                           # Make a deep-copy of that list using slicing
                           L2 = L1[:]
                           # Sort the original list using e.g. `sort_halfsorted(L, bubble)`
                           sort_halfsorted(L1, insertion)
                           # Test that the original list is now sorted
                           self.assertTrue(is_sorted(L1))
                           # Test that the original list and the deep copy have the same elements
                           self.assertCountEqual(L1, L2)

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()

