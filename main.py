from bank.bank import Bank
from bank.custom_exceptions import *
from simple_term_menu import TerminalMenu
from termcolor import colored

bank = Bank()

while True:
    print(colored('\n###----- BANK MENU -----###', 'light_magenta', attrs=['bold']))
    options = ['Create account', 
               'Login', 
               'Exit', ]
    terminal_menu = TerminalMenu(options)
    choice = terminal_menu.show()

    try:
        if choice == 0:
           first_name = input('Enter your first name: ') 
           last_name = input('Enter your last name: ') 
           password = input('Enter your password: ') 
           new_customer = bank.add_customer(first_name, last_name, password)
           print(colored(f'Customer added with ID {new_customer.id}', 'green'))

           saving_acc = ['Create saving account', 'Not now']
           saving_acc_terminal_menu = TerminalMenu(saving_acc)
           s_choice = saving_acc_terminal_menu.show()
           if s_choice == 0:
              print(colored(bank.create_saving_account(new_customer.id), 'green'))

           elif s_choice == 1:
              print(colored('You can create saving account later.', 'yellow'))
              
        elif choice == 1:
            customer_id = input('Enter customer ID: ')
            customer_password = input('Enter customer password: ')
            bank.login(customer_id, customer_password)

            while True:
                print(colored('\n--- Account Menu ---', 'light_magenta', attrs=['bold']))
                l_options = ['Deposit', 
                             'Withdraw', 
                             'Tranasfer between accounts', 
                             'Tranasfer to other customer', 
                             'View transactions',
                             'Create saving account',
                             'Logout', ]
                
                acc_terminal_menu = TerminalMenu(l_options)
                l_choice = acc_terminal_menu.show()

                if l_choice == 0:
                    deposit = ['Deposit to Checking', 'Deposit to Saving']
                    deposit_terminal_menu = TerminalMenu(deposit)
                    d_choice = deposit_terminal_menu.show()
                    if d_choice == 0:
                        amount = float(input('Enter amount: '))
                        print(colored(bank.deposit('Checking', amount), 'green'))
                    elif d_choice == 1:
                        amount = float(input('Enter amount: '))
                        print(colored(bank.deposit('Saving', amount), 'green'))
              
                elif l_choice == 1:
                    withdraw = ['Withdraw from Checking', 'Withdraw from Saving']
                    withdraw_terminal_menu = TerminalMenu(withdraw)
                    w_choice = withdraw_terminal_menu.show()
                    if w_choice == 0:
                        amount = float(input('Enter amount: '))
                        print(colored(bank.withdraw('Checking', amount), 'green'))
                    elif w_choice == 1:
                        amount = float(input('Enter amount: '))
                        print(colored(bank.withdraw('Saving', amount), 'green'))
      
                elif l_choice == 2:
                    transfer = ['Transfer from Checking to Saving', 'Transfer from Saving to Checking']
                    transfer_terminal_menu = TerminalMenu(transfer)
                    t_choice = transfer_terminal_menu.show()
                    if t_choice == 0:
                        amount = float(input('Enter amount: '))
                        print(colored(bank.transfer_between_accounts('Checking', 'Saving', amount), 'green'))
                    elif t_choice == 1:
                        amount = float(input('Enter amount: '))
                        print(colored(bank.transfer_between_accounts('Saving', 'Checking', amount), 'green'))

                elif l_choice == 3:
                    to_customer = input('Enter target customer ID: ')
                    amount = float(input('Enter amount: '))
                    print(colored(bank.transfer_to_customer(to_customer, amount), 'green'))

                elif l_choice ==4:
                    transactions = bank.transaction_history.get_transactions(bank.logged_in_customer.id)
                    if not transactions:
                        print(colored('No transactions found.', 'red'))
                    else:
                        print(colored('\n--- Transaction History ---', 'light_magenta', attrs=['bold']))
                        for i, t in enumerate(transactions): # geeksforgeeks > "Enumerate() in Python"
                            print(f"{i}. {t['date']} | {t['type']} | Amount: {t['amount']} | Balance: {t['balance']}")
                        transaction_detail = ['Get transaction detail', 'Exit']
                        transaction_detail_terminal_menu = TerminalMenu(transaction_detail)
                        t_d_choice = transaction_detail_terminal_menu.show()

                        if t_d_choice == 0:
                            index = int(input('Enter transaction index: '))
                            detail = bank.transaction_history.get_transaction_details(bank.logged_in_customer.id, index)
                            if detail:
                                print(colored('\n--- Transaction Detail ---', 'light_magenta', attrs=['bold']))
                                print(f"Date: {detail['date']}")
                                print(f"Type: {detail['type']}")
                                print(f"Amount: {detail['amount']}")
                                print(f"Balance: {detail['balance']}")

                            else:
                                print(colored('Transaction not found.', 'red'))
                        elif t_d_choice == 1:
                            continue
                
                elif l_choice == 5:
                    print(colored(bank.create_saving_account(bank.logged_in_customer.id), 'green'))
                
                elif l_choice == 6:
                    print(colored(bank.logout(), 'cyan'))
                    break

        elif choice == 2:
            print(colored('Goodbye!', 'cyan'))
            bank.save_data()
            break
        
    except Exception as e:
        print('Error: ', e)
        
