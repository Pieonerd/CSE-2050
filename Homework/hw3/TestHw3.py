from hw3 import find_pairs_naive, find_pairs_optimized
import unittest


class TestPairs(unittest.TestCase):
    def setUp(self):
        """Set up function"""
        self.l1 = [5, 4, 3, 2, 1]
        self.l2 = []

        self.t1 = 7
        self.t2 = 0
        self.t3 = 10
        self.t4 = 6
    
    def test_pairs(self):
        """Test cases for both find_pairs_naive and find_pairs_optimized functions"""
        # Regular test
        self.assertSetEqual(find_pairs_naive(self.l1, self.t1), {(5, 2), (4, 3)})
        self.assertSetEqual(find_pairs_optimized(self.l1, self.t1), {(5, 2), (4, 3)})
        # Empty list
        self.assertSetEqual(find_pairs_naive(self.l2, self.t1), set())
        self.assertSetEqual(find_pairs_optimized(self.l2, self.t1), set())
        # Target = 0
        self.assertSetEqual(find_pairs_naive(self.l1, self.t2), set())
        self.assertSetEqual(find_pairs_optimized(self.l1, self.t2), set())
        # No Pairs
        self.assertSetEqual(find_pairs_naive(self.l1, self.t3), set())
        self.assertSetEqual(find_pairs_optimized(self.l1, self.t3), set())
        # No Duplicates
        self.assertSetEqual(find_pairs_naive(self.l1, self.t4), {(5, 1), (4, 2)})
        self.assertSetEqual(find_pairs_optimized(self.l1, self.t4), {(5, 1), (4, 2)})


unittest.main()
