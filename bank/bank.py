import csv
from customer import Customer
from account import Account

class Bank:
    def __init__(self):
        self.bank_file = "bank.csv"
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
        new_id = str(max(int(s) for s in self.customers.keys()) + 1 ) # stackoverflow > "Get max key in dictionary"
        new_customer = Customer(new_id, first_name, last_name, password)

        # create default checking account
        checking_account = Account(new_id, 0, 'Checking')
        new_customer.add_account(checking_account)

        # add new customer to customers dict
        self.customers[new_id] = new_customer
        return f'New customer added : {new_customer}'





