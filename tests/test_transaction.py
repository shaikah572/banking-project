import unittest
import os
from bank.transaction import Transaction

class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_transactions.csv'
        self.history = Transaction(self.test_file)

    def tearDown(self):
        os.remove(self.test_file)

    def test_store_transaction(self):
        self.history.store_transactions('1', 'deposit', 200, 1200)
        transaction = self.history.get_transactions('1')
        self.assertEqual(len(transaction), 1)
        self.assertEqual(transaction[0]['type'], 'deposit')
        self.assertEqual(transaction[0]['amount'], '200')

    def test_multiple_transactions(self):
        self.history.store_transactions('2', 'deposit', 100, 1100)
        self.history.store_transactions('2', 'withdraw', 50, 1050)
        transaction = self.history.get_transactions('2')
        self.assertEqual(len(transaction), 2)
        self.assertEqual(transaction[1]['type'], 'withdraw')

    def test_transaction_details(self):
        self.history.store_transactions('3', 'deposit', 500, 1500)
        self.history.store_transactions('3', 'withdraw', 200, 1300)
        detail = self.history.get_transaction_details('3', 1)
        self.assertEqual(detail['type'], 'withdraw')
        self.assertEqual(detail['balance'], '1300')

