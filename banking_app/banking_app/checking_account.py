# for importing Account class to inherit parent class
from account import Account

# Checking Account class that inherits from Account
class CheckingAccount(Account):
    
    # this function is for initializing checking account with transaction fee
    def __init__(self, accountName, accountNumber, initialBalance):
        # calling parent class constructor
        super().__init__(accountName, accountNumber, initialBalance)
        # setting transaction fee for checking accounts
        self.__transactionFee = 1.50
    
    # this function is for overriding withdraw method to include transaction fee
    def withdraw(self, amount):
        # calculating total amount with fee
        totalAmount = amount + self.__transactionFee
        # checking if account has enough money including fee
        if totalAmount > self.checkBalance():
            print(f"error no money in your account to withdraw need {totalAmount:.2f} including {self.__transactionFee:.2f} fee")
            return False
        
        # minus amount from balance
        self._Account__balance = self._Account__balance - amount
        # minus transaction fee from balance
        self._Account__balance = self._Account__balance - self.__transactionFee
        # recording withdrawal transaction
        self.addTransaction("Withdrawal", amount)
        # recording fee transaction
        self.addTransaction("Transaction Fee", self.__transactionFee)
        print(f"Withdrew {amount:.2f} (Fee: {self.__transactionFee:.2f})")
        return True

