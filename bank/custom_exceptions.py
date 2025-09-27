
class BankError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class AuthenticationError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class AccountInactiveError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class OverdraftError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class CustomerNotFoundError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)

class PasswordError(Exception):
    def __init__(self, message=''):
        self.message = message
        super().__init__(self.message)