import unittest
from BET import BETNode, create_trees, find_solutions


class TestBETNode(unittest.TestCase):
    def test_repr(self):
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self):
        """Tests for evaluate() method"""
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4
           
        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))

        # Asserts if tree is equal to -5
        self.assertEqual(root.evaluate(), -5)

    def test_evaluate_tree2(self):
        """Tests for evaluate() method"""
        r"""String representation
               +
              / \
             J   *
                / \
               7   -
                  / \
                 5   J
           
        """
        root = BETNode('+')
        root.add_left(BETNode('J'))
        root.add_right(BETNode('*'))
        root.right.add_left(BETNode('7'))
        root.right.add_right(BETNode('-'))
        root.right.right.add_left(BETNode('5'))
        root.right.right.add_right(BETNode('J'))

        # Asserts if tree evaluates to -31
        self.assertEqual(root.evaluate(), -31)


class TestCreateTrees(unittest.TestCase):
    def test_hand1(self):
        """Tests for create_trees() method"""
        # Asserts that there are 7680 possible solutions
        self.assertEqual(len(create_trees(['A', '2', '3', '4'])), 7680)
        
    def test_hand2(self):
        """Tests for create_trees() method"""
        # Asserts that there are 7680 possible solutions
        self.assertEqual(len(create_trees(['5', '7', '9', 'J'])), 7680)
        
class TestFindSolutions(unittest.TestCase):
    def test0sols(self):
        """Tests for the find_solutions() method when there are no possible solutions"""
        self.assertEqual(len(find_solutions(['A', 'A', 'A', 'A'])), 0)

    def test_A23Q(self):
        """Tests for the find_solutions method for the card list ['A', '2', '3', 'Q']"""
        self.assertEqual(len(find_solutions(['A', '2', '3', 'Q'])), 33)
        
unittest.main()