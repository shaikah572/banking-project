from bank.bank import Bank
from bank.custom_exceptions import *

bank = Bank()

while True:
    print('\n###----- BANK MENU -----###')
    print('1. Add Customer')
    print('2. Create Saving Account')
    print('Q. Exit')
    choice = input('Enter your option: ')

    try:
        if choice == '1':
           first_name = input('Enter your first name: ') 
           last_name = input('Enter your last name: ') 
           password = input('Enter your password: ') 
           new_customer = bank.add_customer(first_name, last_name, password)
           print(f'Customer added with ID {new_customer.id}')

        elif choice == '2':
            customer_id = input('Enter your bank ID: ')
            print(bank.create_saving_account(customer_id))
        
        elif choice.upper() == 'Q':
            print('Goodbye!')
            break

        else: 
            print('Invalid choice')
        
    except Exception as e:
        print('Error: ', e)
        
