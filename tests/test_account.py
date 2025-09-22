import unittest
from bank.account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account_s = Account(1000, 2000, 'Saving')
        self.account_c = Account(1000, 1000, 'Checking')

    def test_create_account_object(self):
        self.assertEqual(self.account_s.owner_id, 1000)
        self.assertEqual(self.account_s.balance, 2000)
        self.assertEqual(self.account_s.type, 'Saving')
        self.assertEqual(self.account_c.owner_id, 1000)
        self.assertEqual(self.account_c.balance, 1000)
        self.assertEqual(self.account_c.type, 'Checking')
    
