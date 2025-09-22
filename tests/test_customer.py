import unittest
from bank.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(1000, 'Shaikah', 'Alrubayan', '16@Bs88hJ')
    
    def test_create_customer_object(self):
        self.assertEqual(self.customer.id, 1000)
        self.assertEqual(self.customer.first_name, 'Shaikah')
        self.assertEqual(self.customer.last_name, 'Alrubayan')
        self.assertEqual(self.customer.password, '16@Bs88hJ')
