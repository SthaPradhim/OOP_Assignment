# function is for displaying formatted transaction history for an account
def displayTransactionHistory(account):
    # getting transaction history from account
    transactions = account.getTransactionHistory()
    
    # checking if there are any transactions
    if len(transactions) == 0:
        print("No transactions found")
        return
    
    print("\n--------------------------------")
    print("TRANSACTION HISTORY")
    print("--------------------------------")
    print("Type                Amount           Balance          Time")
    print("--------------------------------")
    
    # looping through each transaction
    for transaction in transactions:
        transactionType = transaction["type"]
        amount = transaction["amount"]
        balance = transaction["balance"]
        time = transaction["time"]
        # displaying each transaction
        print(f"{transactionType}                {amount:.2f}           {balance:.2f}           {time}")
    
    print("--------------------------------\n")


# function is for getting a valid positive number from user input
def getValidAmount(prompt):
    try:
        # getting input from user
        userInput = input(prompt)
        # converting to float 
        amount = float(userInput)
        # checking if amount is positive means user has money 
        if amount < 0:
            print("error amount should be greater than 0")
            return None
        return amount
    except ValueError:
        print("error please input a valid number")
        return None


# function is for getting a valid account number from user
def getValidAccountNumber(bank):
    try:
        # getting input from user
        userInput = input("Please input account number: ")
        # converting to integer
        accountNumber = int(userInput)
        # checking if account exists
        account = bank.getAccount(accountNumber)
        if account is None:
            print("error account not found")
            return None
        return accountNumber
    except ValueError:
        print("error please input a valid account number")
        return None

