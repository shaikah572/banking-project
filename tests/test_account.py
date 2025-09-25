import unittest
from bank.account import Account
from bank.custom_exceptions import *

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_s = Account(1000, 200, 'Saving')
        self.account_c = Account(1000, 100, 'Checking')

    def test_create_account_object(self):
        self.assertEqual(self.account_s.owner_id, 1000)
        self.assertEqual(self.account_s.balance, 200)
        self.assertEqual(self.account_s.type, 'Saving')
        self.assertEqual(self.account_c.owner_id, 1000)
        self.assertEqual(self.account_c.balance, 100)
        self.assertEqual(self.account_c.type, 'Checking')

    def test_deposit(self):
        self.account_c.deposit(50)
        self.assertEqual(self.account_c.balance, 150)
    
    def test_deposit_reactivate_account(self):
        # set inactive account
        inactive_account = Account(10001, 0, 'Checking')
        inactive_account.balance = -100
        inactive_account.is_active = False

        # bring balance to 100
        inactive_account.deposit(200)

        # check if reactivated
        self.assertTrue(inactive_account.is_active)

    def test_withdraw(self):
        self.account_c.withdraw(50)
        self.assertEqual(self.account_c.balance, 50)
    
    def test_withdraw_inactive_account(self):
        self.account_c.is_active = False
        with self.assertRaises(AccountInactiveError):
            self.account_c.withdraw(50)

    def test_withdraw_past_overdraft_limit(self):
        with self.assertRaises(OverdraftError):
            self.account_c.withdraw(201)
    
    def test_withdraw_overdraft_count_increase(self):
        self.account_c.withdraw(150)

        # overdraft -50 + overdrafft fee -35 = -85
        self.assertEqual(self.account_c.balance, -85)
        self.assertEqual(self.account_c.overdraft_count, 1)
    
    def test_withdraw_deactivate_account(self):
        self.account_c.withdraw(110) # balance = -45
        self.account_c.withdraw(20) # balance = -100
        self.assertFalse(self.account_c.is_active)

    
