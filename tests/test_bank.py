import unittest
from bank.bank import Bank
from bank.custom_exceptions import *

class TestBank(unittest.TestCase):
    def setUp(self):
       self.bank = Bank()
       
    # unittest — Unit testing framework -> https://docs.python.org/3/library/unittest.html
    def test_add_customer(self):
        # check if customer added to customers dict 
        before_added = len(self.bank.customers)
        add_new_customer = self.bank.add_customer('Shaikah', 'Alrubayan', 'Pass123@Aa')
        after_added = len(self.bank.customers)
        self.assertEqual(after_added, before_added+1)

        # check if created checing account for added customer
        new_id = str(max(int(s) for s in self.bank.customers.keys()))
        new_customer = self.bank.customers[new_id]
        self.assertEqual(new_customer.accounts[0].type, 'Checking')
    
    def test_create_saving_account(self):
        # get customer ID and create saving accounnt
        get_id = str(max(int(s) for s in self.bank.customers.keys()))
        self.bank.create_saving_account(get_id)

        # check if saving account created for customer
        saving_account_customer = self.bank.customers[get_id]
        self.assertEqual(saving_account_customer.accounts[1].type, 'Saving')

    def test_create_saving_account_invalid_customer(self):
        with self.assertRaises(CustomerNotFoundError):
            self.bank.create_saving_account('1')