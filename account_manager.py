# -*- coding: utf-8 -*-
"""
Created on sun Dec 29  2024

@author: khushi visaveliya
"""

import hashlib
from utils import write_account, read_accounts

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    account_number = str(100000 + len(read_accounts()))  # Simple account number generation
    password = hash_password(input("Enter a password for your account: "))
    transaction_password = hash_password(input("Set a transaction password: "))
    
    write_account(account_number, name, password, transaction_password, initial_deposit)
    print(f"Your account number: {account_number} (Save this for login)")
    print("Account created successfully!")

def login(accounts):
    account_number = input("Enter your account number: ")
    password = hash_password(input("Enter your password: "))
    
    if account_number in accounts and accounts[account_number]['password'] == password:
        print("Login successful!")
        return account_number
    else:
        print("Invalid account number or password.")
        return None
