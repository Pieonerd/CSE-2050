import unittest, random
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort


class Test_linear_scan(unittest.TestCase):
    def test_linear_scan(self):
        "Tests for linear scan method"
        n = int(1E5)
        # Edge case - sorted list
        L = [(n+i) for i in range(n)]
        self.assertEqual(linear_scan(L), 'sorted')

        # Edge case - reversed list
        L = [(n-i) for i in range(n)]
        self.assertEqual(linear_scan(L), 'reverse_list')

        # Edge case - at most 5 items out of place
        L = [9, 10, 7, 8, 6, 5, 3, 4, 1, 2]
        self.assertEqual(linear_scan(L), 'insertionsort')

        # Edge case - linear scan does not apply
        L = [9, 10, 7, 8, 6, 5, 3, 4, 1, 2, 0]
        self.assertEqual(linear_scan(L), None)
        
class Test_reverse_list(unittest.TestCase):
    def test_reverse_list(self):
        "Tests if the list is reversed"
        n = int(1E5)
        L = [(n-i) for i in range(n)]
        reverse_list(L)
        self.assertFalse(any(L[i] > L[i+1] for i in range(len(L)-1)))


class Test_insertionsort(unittest.TestCase):
    def test_insertionsort(self):
        "Tests insertion sort method"
        n = int(10)
        L = [(n-i) for i in range(n)]
        random.shuffle(L)
        insertionsort(L)
        self.assertFalse(any(L[i] > L[i+1] for i in range(len(L)-1)))

class Test_quicksort(unittest.TestCase):
    def test_quicksort(self):
        "Tests quick sort method"
        n = int(25)
        L = [(n-i) for i in range(n)]
        random.shuffle(L)
        quicksort(L)
        self.assertFalse(any(L[i] > L[i+1] for i in range(len(L)-1)))

class Test_mergesort(unittest.TestCase):
    def self_mergesort(self):
        "Tests for merge sort method"
        n = int(1E5)
        L = [(n-i) for i in range(n)]
        random.shuffle(L)
        print(L)
        mergesort(L)
        self.assertFalse(any(L[i] > L[i+1] for i in range(len(L)-1)))

class Test_magicsort(unittest.TestCase):
    def self_magic_sort(self):
        "Tests for magic sort method"
        # List is sorted
        n = int(1E5)
        L = [(n+i) for i in range(n)]
        self.assertEqual(magic_sort(L), {'sorted'})

        # list is reversed
        L = [(n-i) for i in range(n)]
        self.assertEqual(magic_sort(L), {'reverse_list'})

        # List uses quicksort, insertionsort, and mergesort
        random.shuffle(L)
        self.assertSetEqual(magic_sort(L), {'quicksort', 'insertionsort', 'mergesort'})

        # List uses insertionsort
        n = 10
        L = [(n+i) for i in range(n)]
        random.shuffle(L)
        self.assertEqual(magic_sort(L), {'insertionsort'})

        # List uses insertionsort and quicksort
        n = 25
        L = [(n+i) for i in range(n)]
        random.shuffle(L)
        self.assertEqual(magic_sort(L), {'insertionsort', 'quicksort'})




unittest.main()