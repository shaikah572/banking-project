from bank.custom_exceptions import *

class Account:
    def __init__(self, owner_id, balance, type ):
        self.owner_id = owner_id
        self.balance = balance
        self.type = type
        self.overdraft_count = 0
        self.is_active = True
    
    # deposit, withdraw methods
    def deposit(self, amount):
        # raise error if account not active
        if not self.is_active:
            raise AccountInactiveError('Account is not active.')
        self.balance += amount

    def withdraw(self, amount):
        # raise error if account not active
        if not self.is_active:
            raise AccountInactiveError('Account is not active.')
        
        # check if it saving account so it not get overdrawn
        if self.type.capitalize() == 'Saving':
            if self.balance - amount < 0:
                raise OverdraftError('Saving account cannot be overdrawn.')
            self.balance -= amount
            return

        # apply overdraft protection if account is < -100
        if self.balance - amount < -100:
            raise OverdraftError('Overdraft limit reached.')
        
        self.balance -= amount

        # apply overdraft protection if account is 0 
        if self.balance < 0:
            self.overdraft_count += 1
            self.balance -= 35

            # don't go beyond -100 + overdraft fee -35 = -135
            if self.balance < -135:
                self.balance = -135

        # deactivate account when overdraft limit is reached
        if self.overdraft_count >= 2:
            self.is_active = False

    def __str__(self):
        return f'\nCustomer ID: {self.owner_id} \nAccount type: {self.type} \nBalance: {self.balance}'
