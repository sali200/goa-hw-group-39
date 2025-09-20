class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance


my_account = BankAccount()
my_account.deposit(150)
my_account.withdraw(40)
print("ბალანსი არის:", my_account.get_balance())





class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("შეკრება:", MathUtil.add(5, 3))
print("გამრავლება:", MathUtil.multiply(4, 6))