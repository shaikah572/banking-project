import csv
from customer import Customer
from account import Account

class Bank:
    def __init__(self):
        self.bank_file = "bank.csv"
        self.customers = {}
    
    # load data
    # add customer 
