class BankAccount:
    def __init__(self, name, int_rate, balance):
        self.int_rate = int_rate
        self.name = name
        if balance == None:
            self.balance = 0
        else: 
            self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.name, "balance =", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1+self.int_rate)
        return self

checking = BankAccount("checking", .0125, 10000)
savings = BankAccount("savings", .035, 20000)

checking.deposit(100).deposit(200).deposit(700).withdraw(1000).yield_interest().display_account_info()
savings.deposit(100).deposit(200).withdraw(100).withdraw(200).withdraw(300).withdraw(700).yield_interest().display_account_info()
