# Bank Management System

A simple command-line banking system written in Python.  

## Getting Started

### Dependencies


   ```bash
   pip3 install simple-term-menu termcolor
   ```

### Installation

   ```bash
   git clone https://github.com/shaikah572/banking-project
   ```


### Executing program

 ```bash
 python3 main.py
 ```

## Usage

### Main menu:

```python
from simple_term_menu import TerminalMenu
from termcolor import colored

    print(colored('\n###----- BANK MENU -----###', 'light_magenta', attrs=['bold']))
    options = ['Create account', 
               'Login', 
               'Exit', ]
    terminal_menu = TerminalMenu(options)
    choice = terminal_menu.show()
```

<img width="299" height="79" alt="Screenshot 2025-09-28 at 6 44 08 AM" src="https://github.com/user-attachments/assets/8f8b76a8-e702-45ba-a24f-ea6e930069e6" />

### Account menu:
```python
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
```

<img width="302" height="125" alt="Screenshot 2025-09-28 at 6 46 56 AM" src="https://github.com/user-attachments/assets/c41cb8b5-7c68-49a6-9703-f886a48976df" />


## Contributing

## License





