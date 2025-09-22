import csv
from customer import Customer
from account import Account

class Bank:
    def __init__(self):
        self.bank_file = "bank.csv"
        self.customers = {}
    
    # load data
    def load_data(self):
       with open(self.bank_file, 'r', newline='')  as file:
           reader = csv.DictReader(file) # stackoverflow > "Creating a dictionary from a csv file?"
           for row in reader:
               current_customer = Customer(row['account_id'], row['frst_name'], row['last_name'], row['password'])
               check_acc = Account(row['account_id'], float(row['balance_checking']), 'Checking')
               save_acc = Account(row['account_id'], float(row['balance_savings']), 'Saving')
               current_customer.add_account(check_acc)
               current_customer.add_account(save_acc)
               self.customers[current_customer.id] = current_customer

               
    # add customer 
