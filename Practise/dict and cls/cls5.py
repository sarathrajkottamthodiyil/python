class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance



a = BankAccount()
# b = BankAccount()
x = a.deposit(500)
y = a.withdraw(200)
x = a.deposit(1000)
print(x)
print(y)
