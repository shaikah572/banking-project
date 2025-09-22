class Customer:
    def __init__(self, id, first_name, last_name, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.accounts = [] # account obj
    
    # add account to the customer method
    