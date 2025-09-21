import unittest
from bank.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(1000, 'Shaikah', 'Alrubayan', '16@Bs88hJ', 1000, 2000)
    
    def test_create_customer_object(self):
        self.assertEqual(self.customer.id, 1000)
        self.assertEqual(self.customer.first_name, 'Shaikah')
        self.assertEqual(self.customer.last_name, 'Alrubayan')
        self.assertEqual(self.customer.password, '16@Bs88hJ')
        self.assertEqual(self.customer.checking, 1000)
        self.assertEqual(self.customer.saving, 2000)

