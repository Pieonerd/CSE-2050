import unittest
from waitlist import Waitlist

class TestWaitlist(unittest.TestCase):
    def setUp(self):
        """Set up method for following test cases"""
        self.waitlist = Waitlist()
        self.waitlist.add_customer('Customer1', '12:00')
        self.waitlist.add_customer('Customer2', '12:00')
        self.waitlist.add_customer('Customer3', '10:00')
        self.waitlist.add_customer('Customer4', '18:00')

    def test_add_customer(self):
        """Tests for the add_customer() method"""
        # General case - adding a customer normally
        self.waitlist.add_customer('Customer5', '12:00')
        self.assertEqual(len(self.waitlist._entries), 5)

        # Adding a customer at an invalid time
        self.waitlist.add_customer('Customer6', '24:00')
        self.assertEqual(len(self.waitlist._entries), 5)

        # Adding a customer at an invalid time
        self.waitlist.add_customer('Customer7', '12:60')
        self.assertEqual(len(self.waitlist._entries), 5)


    def test_peek(self):
        """Tests for the peek() method"""
        # General case - peek and see the first customer in the waitlist
        result = self.waitlist.peek()
        self.assertEqual(str(result), '(\'Customer3\', 10:00)')

        # Peeking into a waitlist with no customers
        self.waitlist._entries.clear()
        result = self.waitlist.peek()
        self.assertTupleEqual(result, (None, None))
        

    def test_seat_customer(self):
        """Tests for the seat_customer() method"""
        # General case - seating a customer
        result = self.waitlist.seat_customer()
        self.assertEqual(str(result), '(\'Customer3\', 10:00)')
        self.assertEqual(len(self.waitlist._entries), 3)

        # Seating customers with the same reservation time
        result = self.waitlist.seat_customer()
        self.assertEqual(str(result), '(\'Customer1\', 12:00)')
        self.assertEqual(len(self.waitlist._entries), 2)

        result = self.waitlist.seat_customer()
        self.assertEqual(str(result), '(\'Customer2\', 12:00)')
        self.assertEqual(len(self.waitlist._entries), 1)

        # General case - seating a customer
        result = self.waitlist.seat_customer()
        self.assertEqual(str(result), '(\'Customer4\', 18:00)')
        self.assertEqual(len(self.waitlist._entries), 0)

        # Seating no customers
        result = self.waitlist.seat_customer()
        self.assertTupleEqual(result, (None, None))

    def test_print_reservation_list(self):
        """Tests for the print_reservation_list() method"""
        # General case - prints all customers in order of their priority
        result = self.waitlist.print_reservation_list()
        self.assertEqual(str(result), '[(\'Customer3\', 10:00), (\'Customer1\', 12:00), (\'Customer2\', 12:00), (\'Customer4\', 18:00)]')

        # Printing a reservation list that contains no customers
        self.waitlist._entries.clear()
        result = self.waitlist.print_reservation_list()
        self.assertListEqual(result, [])

    def test_change_reservation(self):
        """Tests for the change_reservation() method"""
        # General case - changing the reservation time for a specific customer
        self.waitlist.change_reservation('Customer2', '09:00')
        result = self.waitlist.peek()
        self.assertEqual(str(result), '(\'Customer2\', 09:00)')

        # Changing the reservation time for a customer that does not exist
        result = self.waitlist.change_reservation('Customer5', '08:00')
        self.assertFalse(result)

unittest.main()