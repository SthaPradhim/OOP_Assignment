# for transaction time stamps
from datetime import datetime

# Account class to represent a  account
class Account:
    
    # this function is for initializing account with name, number and balance
    def __init__(self, accountName, accountNumber, initialBalance):
        # Store name
        self.__accountName = accountName
        # Store account number which is private
        self.__accountNumber = accountNumber
        # Store current balance which is private
        self.__balance = initialBalance
        # List to store all transactions which is private
        self.__transactionHistory = []
        # Add initial deposit as first transaction
        self.addTransaction("Your initial deposit is = ", initialBalance)
    
    # this function is for adding money to the account
    def deposit(self, amount):
        # checking if amount is positive
        if amount <= 0:
            print("error deposit amount should be greater than 0")
            return False
        
        # Add amount 
        self.__balance = self.__balance + amount
        # Record transaction
        self.addTransaction("Deposit", amount)
        print(f"Deposited {amount:.2f}")
        return True
    
    # function is for removing money from the account
    def withdraw(self, amount):
        # checking if amount is positive
        if amount <= 0:
            print("error withdrawal amount should be greater than 0")
            return False
        
        # checking if account has enough fund
        if amount > self.__balance:
            print("error no money in your account to withdraw")
            return False
        
        # minus amount from balance
        self.__balance = self.__balance - amount
        # Record transaction
        self.addTransaction("Withdrawal", amount)
        print(f"Withdrew {amount:.2f}")
        return True
    
    # function is for getting the account balance
    def checkBalance(self):
        return self.__balance
    
    # function is for adding a transaction to transaction history
    def addTransaction(self, transactionType, amount):
        # gettingdate and time
        currentTime = datetime.now()
        # formatting time as string
        timeString = currentTime.strftime("%Y-%m-%d %H:%M:%S")
        # creating transaction 
        transactionRecord = {
            "type": transactionType,
            "amount": amount,
            "time": timeString,
            "balance": self.__balance
        }
        # adding to transaction history
        self.__transactionHistory.append(transactionRecord)
    
    # function is for getting all transactions for this account
    def getTransactionHistory(self):
        return self.__transactionHistory
    
    # function is for getting the account number which is private
    def getAccountNumber(self):
        return self.__accountNumber
    
    # function is for getting the account name which is private
    def getAccountName(self):
        return self.__accountName
    
    # function is for displaying the account information
    def displayAccountInfo(self):
        print("\n--------------------------------")
        print("ACCOUNT INFORMATION")
        print("--------------------------------")
        print(f"Account Holder: {self.__accountName}")
        print(f"Account Number: {self.__accountNumber}")
        print(f"Current Balance: {self.__balance:.2f}")
        print("--------------------------------\n")

