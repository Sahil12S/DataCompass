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
