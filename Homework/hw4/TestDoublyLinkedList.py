from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        '__contain__ method tests'
        dll1 = DLL(range(10))
        self.assertTrue(5 in dll1)      # Item in DLL
        self.assertFalse(10 in dll1)    # Item not in DLL

    def test_neighbors(self):
        'tests for neighbors method returning the items immediately before and after the node with item'
        dll1 = DLL(range(10))
        self.assertEqual(dll1.neighbors(5), (4, 6))    # General case
        self.assertEqual(dll1.neighbors(0), (None, 1)) # Edge case - head
        self.assertEqual(dll1.neighbors(9), (8, None)) # Edge case - tail
        with self.assertRaises(RuntimeError):          # If item not in DLL
            dll1.neighbors(10)

    def test_remove_item(self):
        'tests for remove_node method removing the node containing an item from the DLL'
        dll1 = DLL(range(10))
        self.assertEqual(f'{dll1.remove_node(5)}', 'Node(5)') # General case
        self.assertEqual(dll1.neighbors(4), (3, 6))
        self.assertEqual(f'{dll1.remove_node(0)}', 'Node(0)') # Edge case - head
        self.assertEqual(dll1.neighbors(1), (None, 2))
        self.assertEqual(f'{dll1.remove_node(9)}', 'Node(9)') # Edge case - tail
        self.assertEqual(dll1.neighbors(8), (7, None))
        self.assertEqual(len(dll1), 7)                        # Checks length
        with self.assertRaises(RuntimeError):                 # If node not in DLL
            dll1.remove_node(10)

unittest.main()
