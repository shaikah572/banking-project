import unittest
import os
from bank.bank import Bank
from bank.custom_exceptions import *


class TestBank(unittest.TestCase):
    # stackoverflow > "What's the best way to unit test functions that handle csv files?"
    def setUp(self):
       self.test_file = 'test_bank.csv'
       with open(self.test_file, 'w', newline='') as file:
            file.write("account_id,frst_name,last_name,password,balance_checking,balance_savings\n")

       self.bank = Bank(self.test_file)
    
    def tearDown(self):
        os.remove(self.test_file)


    # unittest — Unit testing framework -> https://docs.python.org/3/library/unittest.html
    def test_add_customer(self):
        # check if customer added to customers dict 
        before_added = len(self.bank.customers)
        add_new_customer = self.bank.add_customer('Shaikah', 'Alrubayan', 'Pass123@Aa')
        after_added = len(self.bank.customers)
        self.assertEqual(after_added, before_added+1)

        # check if created checing account for added customer
        self.assertEqual(add_new_customer.accounts[0].type, 'Checking')
    
    def test_create_saving_account(self):
        # create customer and get ID
        add_new_customer = self.bank.add_customer('Shaikah', 'Alrubayan', 'Pass123@Aa')
        get_id = add_new_customer.id

        # create saving account
        self.bank.create_saving_account(get_id)

        # check if saving account created for customer
        self.assertEqual(len(self.bank.customers[get_id].accounts), 2)
        self.assertEqual(self.bank.customers[get_id].accounts[1].type, 'Saving')

    def test_create_saving_account_invalid_customer(self):
        with self.assertRaises(CustomerNotFoundError):
            self.bank.create_saving_account('1')

    def test_create_saving_account_already_created(self):
        add_new_customer = self.bank.add_customer('Shaikah', 'Alrubayan', 'Pass123@Aa')
        get_id = add_new_customer.id

        # first time creating saving account
        self.bank.create_saving_account(get_id)

        # tring to create another saving accounnt
        with self.assertRaises(BankError):
            self.bank.create_saving_account(get_id)