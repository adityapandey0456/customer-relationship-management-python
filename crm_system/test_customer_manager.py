import unittest
from customer import Customer
from customer_manager import CustomerManager
from exceptions import DuplicateCustomerError

class TestCRM(unittest.TestCase):
    def setUp(self):
        self.mgr = CustomerManager()
        self.c1 = Customer(101, "Ali", "ali@test.com", "123", "1995-05-15", "Melbourne")

    def test_add_customer(self):
        self.mgr.add_customer(self.c1)
        self.assertEqual(len(self.mgr.customers), 1)

    def test_duplicate_error(self):
        self.mgr.add_customer(self.c1)
        with self.assertRaises(DuplicateCustomerError):
            self.mgr.add_customer(self.c1)

    def test_age_logic(self):
        # Born 1995, in 2026 age should be 31 (or 30 depending on month)
        self.assertTrue(30 <= self.c1.calculate_age() <= 31)

if __name__ == '__main__':
    unittest.main()