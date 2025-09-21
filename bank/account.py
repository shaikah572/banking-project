class Account:
    def __init__(self, id, owner_id, balance, type ):
        self.id = id 
        self.owner_id = owner_id
        self.balance = balance
        self.type = type
        self.overdraft_count = 0
        self.is_active = True
    
