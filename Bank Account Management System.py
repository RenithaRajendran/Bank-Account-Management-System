# Base class for Account
class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.__account_number = account_number   # Encapsulation (Private attribute)
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount} to {self.__account_holder}'s account.")
        else:
            print("Deposit amount should be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount} from {self.__account_holder}'s account.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.__account_holder}, {self.__account_number}, Balance: ${self.__balance})"

# Derived class for Savings Account
class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest of ${interest:.2f} to savings account.")

# Derived class for Checking Account
class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            super().withdraw(amount)
        else:
            print("Exceeded overdraft limit.")

# Example usage:
def main():
    # Creating Savings and Checking accounts
    savings = SavingsAccount("SA123", "John Doe", 1000)
    checking = CheckingAccount("CA456", "Jane Doe", 500)

    # Display account details
    print(savings)
    print(checking)

    # Performing transactions
    savings.deposit(500)
    savings.apply_interest()
    print(f"Savings Balance: ${savings.get_balance()}\n")

    checking.withdraw(700)
    checking.deposit(200)
    print(f"Checking Balance: ${checking.get_balance()}\n")

if __name__ == "__main__":
    main()
