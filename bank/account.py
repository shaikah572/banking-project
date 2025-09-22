class Account:
    def __init__(self, owner_id, balance, type ):
        self.owner_id = owner_id
        self.balance = balance
        self.type = type
        self.overdraft_count = 0
        self.is_active = True
    
    # deposit, withdraw, transer methods
