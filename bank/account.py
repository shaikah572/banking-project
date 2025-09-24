from bank.custom_exceptions import *

class Account:
    def __init__(self, owner_id, balance, type ):
        self.owner_id = owner_id
        self.balance = balance
        self.type = type
        self.overdraft_count = 0
        self.is_active = True
    
    # deposit, withdraw, transer methods
    def deposit(self, amount):
        if not self.is_active:
            raise AccountInactiveError('Account is not active.')
        self.balance += amount

    def __str__(self):
        return f'\nCustomer ID: {self.owner_id} \nAccount type: {self.type} \nBalance: {self.balance}'
