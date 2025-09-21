import random

class Bank:
    def __init__(self):
        customers = {}
        accounts = {}
        id_generator = random.randint(1000, 9999)