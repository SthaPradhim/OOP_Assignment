# for importing account classes
from checking_account import CheckingAccount
from savings_account import SavingsAccount

# Bank class to manage multiple accounts
class Bank:
    
    # this function is for initializing bank with empty account dictionary
    def __init__(self):
        # dictionary to store all accounts key should be account number and value should be account object
        self.__accounts = {}
        # a counter to generate unique account numbers
        self.__accountCounter = 1000
    
    # this function is for creating a new account
    def createAccount(self, accountName, accountType, initialBalance):
        # checking if initial balance is positive means user has money in their account
        if initialBalance < 0:
            print("error initial balance should be greater than 0")
            return None
        
        # generating account number that is unique      
        accountNumber = self.__accountCounter
        # incrementing counter for next account number
        self.__accountCounter = self.__accountCounter + 1
        
        # creating account based on account type checking or savings
        if accountType.lower() == "checking":
            newAccount = CheckingAccount(accountName, accountNumber, initialBalance)
        elif accountType.lower() == "savings":
            newAccount = SavingsAccount(accountName, accountNumber, initialBalance)
        else:
            print("error invalid account type use checking or savings")
            return None
        
        # storing account in dictionary
        self.__accounts[accountNumber] = newAccount
        print(f"\nAccount created successfully")
        print(f"Account Number: {accountNumber}")
        print(f"Account Type: {accountType.capitalize()}")
        return accountNumber
    
    # function is for getting an account by account number
    def getAccount(self, accountNumber):
        # checking if account exists
        if accountNumber in self.__accounts:
            return self.__accounts[accountNumber]
        else:
            return None
    
    # function is for getting all account numbers
    def getAllAccounts(self):
        return list(self.__accounts.keys())
    
    # function is for displaying summary of all accounts
    def displayAllAccounts(self):
        if len(self.__accounts) == 0:
            print("No accounts found")
            return
        
        print("\n--------------------------------")
        print("ALL ACCOUNTS")
        print("--------------------------------")
        # looping through all accounts
        for accountNumber in self.__accounts:
            account = self.__accounts[accountNumber]
            print(f"Account #{accountNumber}: {account.getAccountName()} - {account.checkBalance():.2f}")
        print("--------------------------------\n")

