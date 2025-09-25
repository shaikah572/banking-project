from bank.bank import Bank
from bank.custom_exceptions import *

bank = Bank()

while True:
    print('\n###----- BANK MENU -----###')
    print('1. Create account')
    print('2. Login')
    print('Q. Exit')
    choice = input('Enter your option: ')

    try:
        if choice == '1':
           first_name = input('Enter your first name: ') 
           last_name = input('Enter your last name: ') 
           password = input('Enter your password: ') 
           new_customer = bank.add_customer(first_name, last_name, password)
           print(f'Customer added with ID {new_customer.id}')

           s_choice = input('Do you want a saving account? (y/n): ')
           if s_choice.lower() == 'y':
              print(bank.create_saving_account(new_customer.id))

           elif s_choice.lower() == 'n':
              print('You can create saving account later.')

           else:
              print('Wrong choice')
              
        elif choice == '2':
            customer_id = input('Enter customer ID: ')
            customer_password = input('Enter customer password: ')
            bank.login(customer_id, customer_password)
            while True:
                print('\n--- Account Menu ---')
                print('1. Deposit')
                print('2. Withdraw')
                print('3. Trnasfer between accounts')
                print('4. Trnasfer to other customer')
                print('5. Create saving account')
                print('6. Logout')
                l_choice = input('Enter your option: ')

                if l_choice == '1':
                    acc_type = input('Choice account (Checking/Saving): ')
                    amount = float(input('Enter amount: '))
                    print(bank.deposit(acc_type, amount))
                
                elif l_choice == '2':
                    acc_type = input('Choice account (Checking/Saving): ')
                    amount = float(input('Enter amount: '))
                    print(bank.withdraw(acc_type, amount))
                
                elif l_choice == '3':
                    from_acc = input('Choice from which account (Checking/Saving): ')
                    to_acc = input('Choice to which account (Checking/Saving): ')
                    amount = float(input('Enter amount: '))
                    print(bank.tranasfer_between_accounts(from_acc, to_acc, amount))

                elif l_choice == '4':
                    to_customer = input('Enter target customer ID: ')
                    amount = float(input('Enter amount: '))
                    print(bank.transfer_to_customer(to_customer, amount))
                
                elif l_choice == '5':
                    print(bank.create_saving_account(bank.logged_in_customer.id))
                
                elif l_choice == '6':
                    print(bank.logout())
                    break

                else: 
                    print('Invalid choice')

        elif choice.upper() == 'Q':
            print('Goodbye!')
            bank.save_data()
            break

        else: 
            print('Invalid choice')
        
    except Exception as e:
        print('Error: ', e)
        
