class BankAccount:
    def __init__(self, name, acc_type, opening_balance):
        self.holder_name = name
        self._account_type = acc_type
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance


acc = BankAccount("Vedanth", "Savings", 5000)

acc.deposit(int(input("Please enter deposit amount: ")))
acc.withdraw(int(input("Please enter withdrawal amount: ")))

print("Balance:", acc.check_balance())
