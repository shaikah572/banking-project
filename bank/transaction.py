import csv
import os
from datetime import datetime

class Transaction:
    def __init__(self, transaction_file='transactions.csv'):
        self.transaction_file = transaction_file
        self.create_file()
    

    def create_file(self):
        if not os.path.exists(self.transaction_file): # geeksforgeeks > "Python - How to Check if a file or directory exists"
            with open(self.transaction_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['ID', 'date', 'type', 'amount', 'balance'])
    

    def store_transactions(self, id, type, amount, balance):
        with open(self.transaction_file, 'a', newline='') as file: # stackoverflow > "How to append a new row to an old CSV file in Python?"
            writer = csv.writer(file)
            writer.writerow([
                id,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # geeksforgeeks > "Python strftime() function"
                type,
                amount,
                balance,
            ])
        

    def get_transactions(self, id):
        # store customer transactions in a list
        transaction = []
        with open(self.transaction_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ID'] == str(id):
                    transaction.append(row)
        return transaction


    def get_transaction_details(self, id, index):
        # get transaction details by index
        transaction = self.get_transactions(id)
        if 0 <= index < len(transaction):
            return transaction[index]
        return None
