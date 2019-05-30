class User:
    def __init__(self, name):
        self.username = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print(f"Balance for user {self.username} is {self.balance}.")
        return self

    def transfer_money(self, other_user, amount):
        print(f"Transferring {amount} to {other_user.username}.")
        other_user.make_deposit(amount)
        self.balance -= amount
        return self


smith = User("Smith")
smith.make_deposit(100).make_deposit(
    50).make_withdrawl(120).display_user_balance()

ana = User("Ana")
ana.make_deposit(50).make_deposit(175).make_withdrawl(
    25).make_withdrawl(100).display_user_balance()

john = User("John")
john.make_deposit(250).make_withdrawl(150).make_withdrawl(
    20).make_withdrawl(15).display_user_balance()

ana.transfer_money(smith, 20).display_user_balance()
smith.display_user_balance()


class BankAccount:
    def __init__(self, int_rate=3, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}.")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * (self.int_rate / 100)
        return self


account1 = BankAccount(3.7, 1000)
account1.deposit(100).deposit(150).deposit(50).withdraw(
    525).yield_interest().display_account_info()

account2 = BankAccount(2.5, 500)
account2.deposit(1200).deposit(350).withdraw(150).withdraw(150).withdraw(
    310).withdraw(50).yield_interest().display_account_info()
