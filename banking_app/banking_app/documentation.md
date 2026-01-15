# Banking Application - Code Documentation

## Overview

This banking application is a console-based system that allows users to manage bank accounts. The system supports two types of accounts: checking accounts and savings accounts. Users can create accounts, deposit money, withdraw money, check balances, and view transaction history.

## Classes and Their Purpose

### Account Class

The Account class is the base class that represents a bank account. It contains all the basic functionality that both checking and savings accounts need.

**Attributes:**
- __accountName: stores the name of the account holder (private)
- __accountNumber: stores the unique account number (private)
- __balance: stores the current account balance (private)
- __transactionHistory: a list that stores all transaction records (private)

**Methods:**
- __init__: initializes a new account with name, number, and initial balance
- deposit: adds money to the account balance and records the transaction
- withdraw: removes money from the account balance and records the transaction
- checkBalance: returns the current balance
- addTransaction: adds a new transaction to the transaction history with timestamp
- getTransactionHistory: returns the list of all transactions
- getAccountNumber: returns the account number (accessor method)
- getAccountName: returns the account holder name (accessor method)
- displayAccountInfo: displays formatted account information

### CheckingAccount Class

The CheckingAccount class inherits from the Account class. It adds transaction fees to withdrawals.

**Attributes:**
- __transactionFee: stores the fee amount charged for each withdrawal (private, set to 1.50)

**Methods:**
- __init__: initializes checking account and sets the transaction fee
- withdraw: overrides the parent withdraw method to deduct a transaction fee along with the withdrawal amount

### SavingsAccount Class

The SavingsAccount class inherits from the Account class. It adds interest calculation functionality.

**Attributes:**
- __interestRate: stores the annual interest rate (private, set to 5% or 0.05)

**Methods:**
- __init__: initializes savings account and sets the interest rate
- calculateInterest: calculates and adds interest to the account based on number of months
- getInterestRate: returns the interest rate as a percentage

### Bank Class

The Bank class manages multiple accounts. It handles account creation and provides methods to access accounts.

**Attributes:**
- __accounts: a dictionary that stores all accounts using account number as key (private)
- __accountCounter: a counter that generates unique account numbers starting from 1000 (private)

**Methods:**
- __init__: initializes the bank with empty account dictionary
- createAccount: creates a new checking or savings account and returns the account number
- getAccount: retrieves an account object by account number
- getAllAccounts: returns a list of all account numbers
- displayAllAccounts: displays summary information for all accounts

## Helper Functions

### displayTransactionHistory - Displays all transactions for an account in a formatted table showing type, amount, balance, and time.

### getValidAmount - Gets a valid positive number from user input. Returns None if input is invalid or negative.

### getValidAccountNumber - Gets a valid account number from user input. Checks if the account exists in the bank. Returns None if invalid.

### displayMainMenu - Displays the main menu options for the banking application.

### displayAccountMenu - Displays the account operations menu with options for deposits, withdrawals, and other operations.

### handleAccountOperations - Handles all account-related operations based on user menu choices. Processes deposits, withdrawals, balance checks, and other operations.

### main - The main function that runs the banking application. Creates a Bank instance and manages the main menu loop.

## Object-Oriented Programming Concepts Used

**Encapsulation:** All sensitive data like account numbers, balances, and transaction history are stored as private attributes using double underscore prefix. Public methods are provided to access and modify this data safely.

**Inheritance:** CheckingAccount and SavingsAccount inherit from the Account class. They reuse the base functionality and add their own specific features.

**Method Overriding:** CheckingAccount overrides the withdraw method to add transaction fee functionality.

**Data Hiding:** Private attributes are used throughout to protect sensitive information. Accessor methods are provided when external access is needed.

## Design Choices

**Private Attributes:** Sensitive data is made private using double underscore prefix to prevent direct access. Accessor methods are provided when external access is needed.

**Inheritance Structure:** Account is a base class with common functionality. CheckingAccount and SavingsAccount inherit from it to avoid code duplication and allow easy addition of new account types.

**Transaction History:** All transactions are automatically recorded with timestamps to ensure complete audit trail. Stored as a list of dictionaries for easy access.

**Error Handling:** Input validation is centralized in reusable functions to reduce code duplication and ensure consistent error handling across the application.

**Modular File Structure:** Code is split into separate files by functionality. Each class has its own file, making the code easier to maintain and understand.

**Dictionary for Account Storage:** Bank class uses a dictionary with account number as key for fast lookup and efficient management of multiple accounts.

**Method Overriding:** CheckingAccount overrides the withdraw method to automatically apply transaction fees, preventing errors from forgetting to apply fees.

## File Structure

- account.py: contains the Account base class
- checking_account.py: contains the CheckingAccount class
- savings_account.py: contains the SavingsAccount class
- bank.py: contains the Bank class
- utils.py: contains helper functions for input validation and display
- menu.py: contains menu display and operation handling functions
- main.py: contains the main function that runs the application

