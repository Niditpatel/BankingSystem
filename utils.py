import os
from datetime import datetime  # Import datetime for logging transaction dat
ACCOUNTS_FILE = 'accounts.txt'

def read_accounts():
    """Reads account data from the accounts file and returns a dictionary of accounts."""
    if not os.path.exists( ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, 'r') as file:
        accounts = {}
        for line in file:
            account_number, name, password, transaction_password, balance = line.strip().split(',')
            accounts[account_number] = {
                'name': name,
                'password': password,
                'transaction_password': transaction_password,
                'balance': float(balance)
            }
    return accounts

def write_account(account_number, name, password, transaction_password, balance):
    """Writes a new account to the accounts file."""
    with open(ACCOUNTS_FILE, 'a') as file:
        file.write(f"{account_number},{name},{password},{transaction_password},{balance}\n")

def log_transaction(account_number, transaction_type, amount):
    """Logs a transaction to the transactions file with the current date and time."""
    transaction_file = f'transactions_{account_number}.txt'
    with open(transaction_file, 'a') as file:
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{date}, {transaction_type}, {amount}\n")
