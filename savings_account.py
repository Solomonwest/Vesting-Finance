from account import Account

class SavingsAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        if amount <= 10000:
            super().withdraw(amount)

        elif amount > self.balance:
            print ("Insufficient Balance")

        else:
            print("Amount exceeds limit")

    def deposit(self, amount):
        super().deposit(amount)
