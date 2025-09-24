import unittest
from bank.account import Account
from bank.custom_exceptions import *

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_s = Account(1000, 0, 'Saving')
        self.account_c = Account(1000, 0, 'Checking')

    def test_create_account_object(self):
        self.assertEqual(self.account_s.owner_id, 1000)
        self.assertEqual(self.account_s.balance, 0)
        self.assertEqual(self.account_s.type, 'Saving')
        self.assertEqual(self.account_c.owner_id, 1000)
        self.assertEqual(self.account_c.balance, 0)
        self.assertEqual(self.account_c.type, 'Checking')

    def test_deposit(self):
        self.account_c.deposit(50)
        self.assertEqual(self.account_c.balance, 50)
    
    def test_deposit_inactive_account(self):
        self.account_c.is_active = False
        with self.assertRaises(AccountInactiveError):
            self.account_c.deposit(50)
    
