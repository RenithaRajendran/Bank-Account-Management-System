# Bank Account Management System

A simple Python application that simulates basic banking operations using concepts of Object-Oriented Programming (OOP).

## Key Concepts
- **Classes**: Account, SavingsAccount, CheckingAccount
- **Inheritance**: Specialized account types (savings, checking) inheriting from a base Account class
- **Encapsulation**: Private attributes for account details, access only through methods
- **Polymorphism**: Overriding methods to implement custom behavior for different account types

## Features
- Create Savings and Checking accounts
- Deposit and withdraw funds
- View account balance
- Apply interest (for SavingsAccount)
- Overdraft facility (for CheckingAccount)

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/BankAccountManagementSystem.git
2. Run the Python script:
   python bank_account_management.py
3. Example Output:
    Account(John Doe, SA123, Balance: $1000)
    Account(Jane Doe, CA456, Balance: $500)
    Deposited $500 to John Doe's account.
    Applied interest of $45.00 to savings account.
    Savings Balance: $1545.00
    Withdrew $700 from Jane Doe's account.
    Deposited $200 to Jane Doe's account.
    Checking Balance: $0.00
