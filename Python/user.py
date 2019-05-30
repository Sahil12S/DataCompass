class User:
    def __init__(self, name):
        self.username = name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawl(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"Balance for user {self.username} is {self.balance}.")

    def transfer_money(self, other_user, amount):
        print(f"Transferring {amount} to {other_user.username}.")
        other_user.make_deposit(amount)
        self.balance -= amount

    

smith = User("Smith")
smith.make_deposit(100)
smith.make_deposit(50)
smith.make_withdrawl(120)
smith.display_user_balance()

ana = User("Ana")
ana.make_deposit(50)
ana.make_deposit(175)
ana.make_withdrawl(25)
ana.make_withdrawl(100)
ana.display_user_balance()

john = User("John")
john.make_deposit(250)
john.make_withdrawl(150)
john.make_withdrawl(20)
john.make_withdrawl(15)
john.display_user_balance()

ana.transfer_money(smith, 20)
ana.display_user_balance()
smith.display_user_balance()
