class Customer:
    def __init__(self, id, first_name, last_name, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.accounts = [] # account obj
    
    # add accounts to the customer method
    def add_account(self, account):
        self.accounts.append(account)
    
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return f'\nCustomer ID: {self.id} \nCustomer full name: {self.first_name} {self.last_name} \nBalance: {self.accounts[0].balance}'
    