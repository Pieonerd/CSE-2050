from Cards import Card, Deck, Hand
import unittest


class TestCard(unittest.TestCase):
    "Test cases specific to the Card class"
    def setUp(self):
        """Sets up cards"""
        self.c1 = Card(1, 'clubs')
        self.c2 = Card(1, 'diamonds')
        self.c3 = Card(2, 'clubs')

    def test_init(self):
        """Initialization test"""
        self.assertEqual(self.c1.value, 1)
        self.assertEqual(self.c1.suit, 'clubs')
    
    def test_repr(self):
        """String representation test"""
        self.assertEqual(f'{self.c1}', 'Card(1 of clubs)')

    def test_lt(self):
        """Less than test"""
        self.assertLess(self.c1, self.c2)
        self.assertLess(self.c1, self.c3)
    
    def test_eq(self):
        """Equality test"""
        self.assertNotEqual(self.c1, self.c2)
        self.assertNotEqual(self.c1, self.c3)


class TestDeck(unittest.TestCase):
    "Test cases specific to the Deck class"
    def setUp(self):
        """Sets up deck"""
        self.d1 = Deck([2, 1], ['squares', 'circles'])
    
    def test_init(self):
        """Initialization test"""
        self.assertEqual(str(self.d1.card_list), '[Card(2 of squares), Card(1 of squares), Card(2 of circles), Card(1 of circles)]')

    def test_len(self):
        """Deck length test"""
        self.assertEqual(len(self.d1), 4)

    def test_sort(self):
        """Sorting test"""
        self.assertEqual(f'{self.d1.sort()}', '[Card(1 of circles), Card(2 of circles), Card(1 of squares), Card(2 of squares)]')
    
    def test_repr(self):
        """String representation test"""
        self.assertEqual(f'{self.d1}', 'Deck: [Card(2 of squares), Card(1 of squares), Card(2 of circles), Card(1 of circles)]')

    def test_shuffle(self):
        """Deck shuffling test"""
        self.assertNotEqual(f'{self.d1.shuffle()}', '[Card(1 of circles), Card(2 of circles), Card(1 of squares), Card(2 of squares)]')

    def test_draw(self):
        """Draw card test"""
        self.assertEqual(f'{self.d1.draw_top()}', f'Card(1 of circles)')


class TestHand(unittest.TestCase):
    "Card cases specific to the Hand class"
    def setUp(self):
        """Sets up hand"""
        self.h_dots = Hand([Card(value, 'dots') for value in range(5, 0, -1)])
    
    def test_init(self):
        """Initialization test"""
        self.assertEqual(str(self.h_dots.card_list), '[Card(5 of dots), Card(4 of dots), Card(3 of dots), Card(2 of dots), Card(1 of dots)]')

    def test_repr(self):
        """String representation test"""
        self.assertEqual(f'{self.h_dots}', 'Hand: [Card(5 of dots), Card(4 of dots), Card(3 of dots), Card(2 of dots), Card(1 of dots)]')

    def test_play(self):
        """Play test"""
        self.assertEqual(str(self.h_dots.play(Card(1, 'dots'))), 'Card(1 of dots)')
        with self.assertRaises(RuntimeError):
            self.h_dots.play(Card(1, 'hearts'))


unittest.main()