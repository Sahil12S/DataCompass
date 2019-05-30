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


class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        self.account = dict()

    def add_bank_account(self, account_name, int_rate=2, balance=0):
        if account_name not in self.account.keys():
            self.account[account_name] = BankAccount(
                int_rate=int_rate, balance=balance)
        else:
            print("Account already exists")
        return self

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(amount)
        return self

    def make_withdrawl(self, amount, account_name):
        self.account[account_name].withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"Account balances for user {self.username} are:")
        for key, value in self.account.items():
            print(f"Account: {key}")
            self.account[key].display_account_info()
        return self

    def transfer_money(self, other_user, amount, sender_account_name, receiver_account_name):
        print(f"Transferring {amount} to {other_user.username}.")
        other_user.make_deposit(amount, receiver_account_name)
        self.account[sender_account_name].withdraw(amount)
        return self


smith = User("Smith", "smith@gmail.com")
smith.add_bank_account("savings").add_bank_account(
    "current", int_rate=1.7, balance=100)
smith.make_deposit(100, "savings").make_deposit(
    250, "current").make_withdrawl(20, "savings").display_user_balance()

print("="*50)

ana = User("Ana", "ana@yahoo.com")
ana.add_bank_account("savings", balance=300).add_bank_account(
    "current", int_rate=1.7, balance=1000)
ana.make_deposit(50, "current").make_deposit(175, "savings").make_withdrawl(
    25, "current").make_withdrawl(100, "savings").display_user_balance()

print("="*50)

john = User("John", "john@gmail.com")
john.add_bank_account("savings", int_rate=3.5, balance=250).add_bank_account(
    "current", int_rate=2.7, balance=400)
john.make_deposit(250, "savings").make_withdrawl(150, "current").make_withdrawl(
    20, "savings").make_withdrawl(15, "savings").display_user_balance()

print("="*50)

ana.transfer_money(smith, 20, "savings", "savings").display_user_balance()
smith.display_user_balance()


# account1 = BankAccount(3.7, 1000)
# account1.deposit(100).deposit(150).deposit(50).withdraw(
#     525).yield_interest().display_account_info()

# account2 = BankAccount(2.5, 500)
# account2.deposit(1200).deposit(350).withdraw(150).withdraw(150).withdraw(
#     310).withdraw(50).yield_interest().display_account_info()
