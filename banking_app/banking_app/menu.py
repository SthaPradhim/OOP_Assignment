# for importing utility functions
from utils import getValidAmount, getValidAccountNumber, displayTransactionHistory
# for importing SavingsAccount to check account type
from savings_account import SavingsAccount

# function is for displaying the main menu options
def displayMainMenu():
    print("\n--------------------------------")
    print("BANKING APPLICATION - MAIN MENU")
    print("--------------------------------")
    print("1. Create New Account")
    print("2. Select Account")
    print("3. View All Accounts")
    print("4. Exit")
    print("--------------------------------")


# function is for displaying the account operations menu
def displayAccountMenu():
    print("\n--------------------------------")
    print("ACCOUNT OPERATIONS")
    print("--------------------------------")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. View Transaction History")
    print("5. View Account Information")
    print("6. Calculate Interest (Savings Only)")
    print("7. Back to Main Menu")
    print("--------------------------------")


# function is for handling all account-related operations
def handleAccountOperations(bank, accountNumber):
    # getting the account object
    account = bank.getAccount(accountNumber)
    
    # keeping menu showing until user did not choose to go back to main menu
    while True:
        # displaying account menu
        displayAccountMenu()
        # getting user choice
        choice = input("Please input your choice (1-7): ").strip()
        
        # processing deposit
        if choice == "1":
            amount = getValidAmount("Please input deposit amount: ")
            if amount is not None:
                account.deposit(amount)
        
        # processing withdrawal
        elif choice == "2":
            amount = getValidAmount("Please input withdrawal amount: ")
            if amount is not None:
                account.withdraw(amount)
        
        # checking balance
        elif choice == "3":
            balance = account.checkBalance()
            print(f"\nCurrent Balance: {balance:.2f}\n")
        
        # viewing transaction history
        elif choice == "4":
            displayTransactionHistory(account)
        
        # viewing account information
        elif choice == "5":
            account.displayAccountInfo()
        
        # calculating interest (for savings accounts only)
        elif choice == "6":
            if isinstance(account, SavingsAccount):
                monthsInput = input("Please input number of months for interest calculation: ")
                try:
                    months = int(monthsInput)
                    if months > 0:
                        account.calculateInterest(months)
                    else:
                        print("error months should be greater than 0")
                except ValueError:
                    print("error please input a valid number")
            else:
                print("error interest calculation is only available for Savings accounts")
        
        # going back to main menu
        elif choice == "7":
            break
        
        # invalid choice
        else:
            print("error invalid choice please select 1-7")

