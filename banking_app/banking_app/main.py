# for importing Bank class
from bank import Bank
# for importing menu functions
from menu import displayMainMenu, handleAccountOperations
# for importing utility functions
from utils import getValidAmount, getValidAccountNumber

# function is for running the banking application main function
def main():
    # creating bank instance
    bank = Bank()
    
    print("Welcome to the Banking Application")
    print("This application helps you manage your bank accounts")
    
    # keeping main menu showing until user exits
    while True:
        # displaying main menu
        displayMainMenu()
        # getting user choice
        choice = input("Please input your choice (1-4): ").strip()
        
        # creating new account
        if choice == "1":
            # getting account holder name
            accountName = input("Please input account holder name: ").strip()
            if not accountName:
                print("error account name cannot be empty")
                continue
            
            # getting account type
            accountType = input("Please input account type (checking/savings): ").strip()
            if accountType.lower() not in ["checking", "savings"]:
                print("error account type must be checking or savings")
                continue
            
            # getting initial balance
            initialBalance = getValidAmount("Please input initial balance: ")
            if initialBalance is not None:
                bank.createAccount(accountName, accountType, initialBalance)
        
        # selecting account for operations
        elif choice == "2":
            # checking if any accounts exist
            if len(bank.getAllAccounts()) == 0:
                print("No accounts found please create an account first")
                continue
            
            # getting account number
            accountNumber = getValidAccountNumber(bank)
            if accountNumber is not None:
                # handling account operations
                handleAccountOperations(bank, accountNumber)
        
        # viewing all accounts
        elif choice == "3":
            bank.displayAllAccounts()
        
        # exiting application
        elif choice == "4":
            print("\nThank you for using the Banking Application Goodbye")
            break
        
        # invalid choice
        else:
            print("error invalid choice please select 1-4")


# running the application when script is executed
if __name__ == "__main__":
    main()

