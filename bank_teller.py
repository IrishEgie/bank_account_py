class BankAccount:

    # TODO: Define the __init__ method with parameters for the account holder's name and initial balance.
    def __init__(self, owner, balance):
        # TODO: Set attributes for the owner's name and the initial balance.
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # TODO: Add the 'amount' to the balance attribute.
        self.balance += amount
        # TODO: Print a confirmation message with the new balance.
        print(f"Deposit Transaction Compeleted, New Balance is: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        # TODO: Check if the account has enough balance.
        if self.balance<amount:
            print("We are sorry, this account does not have enough balance to complete this transaction: ")
            return False
        # TODO: If yes, subtract the amount from the balance and print a confirmation message.
        print(f"Transaction processing ...\nYou have withdrawn: P{round(amount,2)}")
        self.balance-=amount
        self.display_balance()
        return self.balance
        # TODO: If no, print a message saying insufficient funds.
        
    def display_balance(self):
        """ Print the current balance of the account."""
        print(f"Account Name: {self.owner}\nCurrent Balance: P{self.balance}")
        return self.balance
        
        
