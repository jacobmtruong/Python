# Assignment: BankAccount
# Learning Objectives:

# Students will follow specifications for creating a class.
# Students will implement default arguments in parameters for attributes that can be assigned on instantiation.
# Students will use basic programmatic logic to implement the functionality of a bank account
# Students will handle edge-cases, such as insufficient funds, with the appropriate control structure (if-else, code flow, or early exit)
# Students will demonstrate proficiency in creating and update attributes of an object instance, from within the class using self .
# Students will thoroughly test the functionality of their class by creating instances and calling methods with different test data and scenarios.

# If you imagine a banking system, and how the data is modeled, you may think, well, everything should be tied to the customer, in other words, the user. But users have accounts, and accounts have balances. This gives us the idea that maybe an account is its own class apart from the user class. But as we stated, it is not completely independent of the User class; accounts only exist because users open them.

# For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!

# Let's first just get some more practice writing classes by writing a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


# deposit(self, amount) - increases the account balance by the given amount

    def deposit(self, amount):
        self.balance += amount
        return self

# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            print(f"This is your current balance: {self.balance}")
        return self    

# display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self


# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate
            print(f"Balance: ${self.balance}")
        return self