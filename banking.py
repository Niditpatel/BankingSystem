# -*- coding: utf-8 -*-
"""
Created on sun Dec 29  2024

@author: khushi visaveliya
"""
from account_manager import create_account, login
from transaction_manager import deposit, withdraw, check_balance, view_transaction_history
from utils import read_accounts

def main():
    accounts = read_accounts()
    
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            account_number = login(accounts)
            if account_number:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. View Transaction History")
                    print("5. Logout")
                    transaction_choice = input("Enter your choice: ")
                    
                    if transaction_choice == '1':
                        deposit(accounts, account_number)
                    elif transaction_choice == '2':
                        withdraw(accounts, account_number)
                    elif transaction_choice == '3':
                        check_balance(accounts, account_number)
                    elif transaction_choice == '4':
                        view_transaction_history(account_number)
                    elif transaction_choice == '5':
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == '3':
            print("Thank you for using the Banking System!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
