import csv
from bank.customer import Customer
from bank.account import Account
from bank.custom_exceptions import *
from bank.transaction import Transaction
import re


class Bank:
    def __init__(self, bank_file = 'bank.csv'):
        self.bank_file = bank_file
        self.customers = {}
        self.logged_in_customer = None
        self.transaction_history = Transaction()
        self.load_data() 
        

    #--------- Load Data
    def load_data(self):
       with open(self.bank_file, 'r', newline='')  as file:
           reader = csv.DictReader(file) # stackoverflow > "Creating a dictionary from a csv file?"
           for row in reader:
               
               # get customer information from csv 
               current_customer = Customer(row['account_id'], row['first_name'], row['last_name'], row['password'])
               
               # create checking and saving account
               check_acc = Account(row['account_id'], float(row['balance_checking']), 'Checking')
               save_acc = Account(row['account_id'], float(row['balance_savings']), 'Saving')
               current_customer.add_account(check_acc)
               current_customer.add_account(save_acc)

               # get active status and overdraft count
               active_acc = row.get('active', 'True') # stackoverflow > "Return a default value if a dictionary key is not available"
               check_acc.is_active = active_acc.lower() == 'true'
               overdrafts_acc = row.get('overdrafts', '0')
               check_acc.overdraft_count = int(overdrafts_acc)

               # save customer in customers dict
               self.customers[current_customer.id] = current_customer
    #--------------------------- 


    #--------- Management
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
            raise CustomerNotFoundError('Customer not found')
        
        # create the saving account 
        customer = self.customers[id]
        if len(customer.accounts) >= 2:
            raise BankError('Saving account already created!')
        
        saving_account = Account(id, 0, 'Saving')
        customer.add_account(saving_account)

        return 'Saving account created.'
    
    def check_password(self, password):  # geeksforgeeks > "Python program to check the validity of a Password"
        if (len(password)<=8):
            raise PasswordError('Password must be longer than 8 characters.')
        if not re.search("[a-z]", password):
            raise PasswordError('Password must contain a lowercase letter.')
        if not re.search("[A-Z]", password):
            raise PasswordError('"Password must contain an uppercase letter.')
        if not re.search("[0-9]", password):
            raise PasswordError('Password must contain a number.')
        if not re.search("[_@$]" , password):
            raise PasswordError('Password must contain at least one special character (_ @ $).')
        if re.search(r"\s" , password):
            raise PasswordError('Password cannot contain spaces.')
        
        return password
    #--------------------------- 


    #--------- Authentication
    def login(self, id, password):
        # check customer ID
        if id not in self.customers:
            raise AuthenticationError('Customer ID not found.')
        
        customer = self.customers[id]

        # check correct password
        if customer.password != password:
            raise AuthenticationError('Incorrect password.')
        
        self.logged_in_customer = customer
        return f'Welcome {customer.get_fullname()}'
    
    def logout(self):
        # if customer logged in then log out
        if self.logged_in_customer:
            self.logged_in_customer = None

        # else raise an error
        else:
            raise BankError('You are not logged in.')
        return "Logged out."
    
    def require_login(self):
        if not self.logged_in_customer:
            raise AuthenticationError('You must log in first.')
    
    #--------------------------- 


    #--------- Transactions
    def deposit(self, account_type, amount):
        # require logging in first
        self.require_login()

        # get account
        customer_account = self.logged_in_customer.get_account(account_type)

        # raise error if account not found
        if not customer_account:
            raise BankError(f'{account_type} account not found.')
        
        customer_account.deposit(amount)

        # store deposit 
        self.transaction_history.store_transactions(customer_account.owner_id, 'deposit', amount, customer_account.balance)

        return f'{amount} deposit into {account_type} account. \nAccount balance: {customer_account.balance}'
    
    def withdraw(self, account_type, amount):
        # require logging in first
        self.require_login()

        # get account
        customer_account = self.logged_in_customer.get_account(account_type)

        # raise error if account not found
        if not customer_account:
            raise BankError(f'{account_type} account not found.')
        
        customer_account.withdraw(amount)

        # store withdraw 
        self.transaction_history.store_transactions(customer_account.owner_id, 'withdraw', amount, customer_account.balance)

        return f'{amount} withdraw from {account_type} account. \nAccount balance: {customer_account.balance}'
    
    def transfer_between_accounts(self, from_type, to_type, amount):
        # require logging in first
        self.require_login()
        
        # get accounts from current customer
        from_account = self.logged_in_customer.get_account(from_type)
        to_account = self.logged_in_customer.get_account(to_type)

        # raise error for wrong account type
        if not from_account or not to_account:
            raise BankError('Invalid account type.')
        
        from_account.withdraw(amount)
        to_account.deposit(amount)

        # store transfer
        self.transaction_history.store_transactions(from_account.owner_id, 'tranasfer_between_accounts', amount, from_account.balance)

        return f'{amount} transferred from {from_type} to {to_type}. \n{from_type} account balance: {from_account.balance} \n{to_type} account balance: {to_account.balance} '
    
    def transfer_to_customer(self, target_id, amount):
        # require logging in first
        self.require_login()

        # raise error if customer not found
        if target_id not in self.customers:
            raise CustomerNotFoundError('Target customer not found.')
        
        # transfer from checking accounts only
        from_account = self.logged_in_customer.get_account('checking')
        to_account = self.customers[target_id].get_account('checking')

        from_account.withdraw(amount)
        to_account.deposit(amount)

        # store tranasfer 
        self.transaction_history.store_transactions(from_account.owner_id, 'tranasfer_to_customer', amount, from_account.balance)

        return f'{amount} transferred from {self.logged_in_customer.id} account to {target_id} account \nAccount balance: {from_account.balance}'
    #--------------------------- 


    #--------- Save Data
    def save_data(self):
        # geeksforgeeks > "Writing CSV files in Python"
        with open(self.bank_file, 'w', newline='') as file:
            fieldnames = ['account_id', 'first_name', 'last_name', 'password', 'balance_checking', 'balance_savings', 'active', 'overdrafts']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for customer in self.customers.values():
                check_acc = customer.get_account('checking')
                save_acc = customer.get_account('saving')
                writer.writerow({
                    'account_id': customer.id,
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'password': customer.password,
                    'balance_checking': check_acc.balance,
                    'balance_savings': save_acc.balance if save_acc else 0,
                    'active': check_acc.is_active,
                    'overdrafts': check_acc.overdraft_count,
                })
    #--------------------------- 
