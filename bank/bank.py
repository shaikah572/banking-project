import csv
from bank.customer import Customer
from bank.account import Account
from bank.custom_exceptions import *


class Bank:
    def __init__(self, bank_file = "bank.csv"):
        self.bank_file = bank_file
        self.customers = {}
        self.load_data() 
    
    # load data
    def load_data(self):
       with open(self.bank_file, 'r', newline='')  as file:
           reader = csv.DictReader(file) # stackoverflow > "Creating a dictionary from a csv file?"
           for row in reader:
               
               # get customer information from csv 
               current_customer = Customer(row['account_id'], row['frst_name'], row['last_name'], row['password'])
               
               # create checking and saving account
               check_acc = Account(row['account_id'], float(row['balance_checking']), 'Checking')
               save_acc = Account(row['account_id'], float(row['balance_savings']), 'Saving')
               current_customer.add_account(check_acc)
               current_customer.add_account(save_acc)

               # save customer in customers dict
               self.customers[current_customer.id] = current_customer

               
    # add customer 
    def add_customer(self, first_name, last_name, password):
        # generate new id and create new customer object
        if self.customers:
            new_id = str(max(int(s) for s in self.customers.keys()) + 1 ) # stackoverflow > "Get max key in dictionary"
        else: 
            new_id = '10001'
        
        new_customer = Customer(new_id, first_name, last_name, password)

        # create default checking account
        checking_account = Account(new_id, 0, 'Checking')
        new_customer.add_account(checking_account)

        # add new customer to customers dict
        self.customers[new_id] = new_customer
        return new_customer
    

    def create_saving_account(self, id):
        # search customer by id in customers dict and raise error if not found
        id = str(id)
        if id not in self.customers:
            raise CustomerNotFoundError('Error! Customer ID not found')
        
        # create the saving account 
        customer = self.customers[id]
        if len(customer.accounts) >= 2:
            raise BankError('Saving account already created!')
        
        saving_account = Account(id, 0, 'Saving')
        customer.add_account(saving_account)

        return 'Saving account created.'
