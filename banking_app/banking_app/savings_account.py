# for importing Account class to inherit
from account import Account

# Savings Account class that inherits from Account
class SavingsAccount(Account):
    
    # this function is for initializing savings account with interest rate
    def __init__(self, accountName, accountNumber, initialBalance):
        # calling parent class constructor
        super().__init__(accountName, accountNumber, initialBalance)
        # setting interest rate for savings accounts (5% per year)
        self.__interestRate = 0.05
    
    # this function is for calculating and adding interest to account
    def calculateInterest(self, months):
        # getting current balance
        currentBalance = self.checkBalance()
        # calculating monthly interest rate
        monthlyRate = self.__interestRate / 12
        # calculating interest for given months
        interestAmount = currentBalance * monthlyRate * months
        # adding interest to balance
        self._Account__balance = self._Account__balance + interestAmount
        # recording interest transaction
        self.addTransaction("Interest", interestAmount)
        print(f"Interest of {interestAmount:.2f} added for {months} months")
        return interestAmount
    
    # function is for getting the interest rate
    def getInterestRate(self):
        return self.__interestRate * 100

