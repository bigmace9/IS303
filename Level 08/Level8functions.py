#Mason Chandler
#Level 08 Assignment

import random
#A template to what something is
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.account_number = random.randint(1, 100)
        self.balance = 0.0




# Make a deposit
def deposit(balance):
    balance = int(balance)
    while True:
        try:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                return f'Remaining Balance: {amount + balance}'
            print("Input must be a number and greater than 0")
        except ValueError:
            print("Input must be a number and greater than 0")

# Make a withdrawal
def withdraw(balance): 
    balance = int(balance)
    while True: 
        try:
            amount = int(input("How much to withdraw: "))
            if amount <= 0:
                print("Input must be a number and greater than 0")
            elif amount > balance:
                print ("Insufficient Funds")
            else:
                return f'Remaining Balance: {balance - amount}'
        except ValueError:
            print("Input must be a number and greater than 0")


# View account information
def view_account(account):
    print(f"Name: {account.name}")
    print(f"Account Number: {account.account_number}")
    print(f"Account Balance: {account.balance:.2f}")