from datetime import datetime
from utils import log_transaction, read_accounts
from account_manager import hash_password  # Import hash_password here

def deposit(accounts, account_number):
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]['balance'] += amount
    log_transaction(account_number, 'Deposit', amount)
    print(f"Deposit successful! Current balance: {accounts[account_number]['balance']}")

def withdraw(accounts, account_number):
    transaction_password = input("Enter your transaction password: ")
    hashed_transaction_password = hash_password(transaction_password)
    
    if hashed_transaction_password != accounts[account_number]['transaction_password']:
        print("Invalid transaction password.")
        return
    
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[account_number]['balance']:
        print("Insufficient balance.")
    else:
        accounts[account_number]['balance'] -= amount
        log_transaction(account_number, 'Withdrawal', amount)
        print(f"Withdrawal successful! Current balance: {accounts[account_number]['balance']}")

def check_balance(accounts, account_number):
    print(f"Your current balance is: {accounts[account_number]['balance']}")

def view_transaction_history(account_number):
    try:
        with open(f'transactions_{account_number}.txt', 'r') as file:
            print("\nTransaction History:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No transaction history found.")
