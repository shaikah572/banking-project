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

       # create default customer
       self.customer = self.bank.add_customer('Shaikah', 'Alrubayan', 'Pass123@Aa')
       self.get_id = self.customer.id
       self.bank.login(self.get_id, 'Pass123@Aa')
    
    def tearDown(self):
        os.remove(self.test_file)


    # unittest — Unit testing framework -> https://docs.python.org/3/library/unittest.html
    def test_add_customer(self):
        # check if customer added to customers dict 
        before_added = len(self.bank.customers)
        add_new_customer = self.bank.add_customer('Norah', 'Alotaibi', 'Exampl3*Fl')
        after_added = len(self.bank.customers)
        self.assertEqual(after_added, before_added+1)

        # check if created checing account for added customer
        self.assertEqual(add_new_customer.accounts[0].type, 'Checking')
    
    def test_create_saving_account(self):
        # create saving account
        self.bank.create_saving_account(self.get_id)

        # check if saving account created for customer
        self.assertEqual(len(self.bank.customers[self.get_id].accounts), 2)
        self.assertEqual(self.bank.customers[self.get_id].accounts[1].type, 'Saving')

    def test_create_saving_account_invalid_customer(self):
        with self.assertRaises(CustomerNotFoundError):
            self.bank.create_saving_account('1')

    def test_create_saving_account_already_created(self):
        # first time creating saving account
        self.bank.create_saving_account(self.get_id)

        # tring to create another saving accounnt
        with self.assertRaises(BankError):
            self.bank.create_saving_account(self.get_id)
    
    def test_login(self):
        # testing if customer is logged in
        self.assertEqual(self.bank.logged_in_customer, self.customer)
    
    def test_login_invalid_id(self):
        with self.assertRaises(AuthenticationError):
            self.bank.login('1', 'Pass123@Aa')
    
    def test_login_wrong_password(self):
        with self.assertRaises(AuthenticationError):
            self.bank.login(self.get_id, 'password')
    
    def test_logout_without_login(self):
        self.bank.logged_in_customer = None
        with self.assertRaises(BankError):
            self.bank.logout()
    
    def test_require_login(self):
        self.bank.logged_in_customer = None
        with self.assertRaises(AuthenticationError):
            self.bank.require_login()
    
    def test_deposit(self):
        before_balance = self.customer.get_account('checking').balance
        self.bank.deposit('checking', 200)
        after_balance = self.customer.get_account('checking').balance

        self.assertEqual(after_balance, before_balance+200)
    
    def test_deposit_require_login(self):
        self.bank.logout()
        with self.assertRaises(AuthenticationError):
            self.bank.deposit('checking', 200)
    
    def test_deposit_invalid_account(self):
        with self.assertRaises(BankError):
            self.bank.deposit('type', 200)