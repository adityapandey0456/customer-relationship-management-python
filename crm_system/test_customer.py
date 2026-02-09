# test_customer.py
import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def test_age_calculation(self):
        customer = Customer(1, "Test", "test@mail.com", "123", "2000-01-01", "Sydney")
        # TODO: expected age assert

if __name__ == "__main__":
    unittest.main()
