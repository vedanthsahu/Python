import datetime


class BankAccount:
    def __init__(self, opening_amount=0):
        self._balance = opening_amount  

    def deposit(self, money):
        if money <= 0:
            print("Deposit amount must be positive.")
            return

        self._balance += money
        print(f"Deposited Rs {money}. New balance: Rs {self._balance}")
        self._log("Deposit", money)

    def withdraw(self, money):
        if money <= 0:
            print("Withdrawal amount must be positive.")
            return

        if money > self._balance:
            print("Insufficient funds!")
            self._log("Failed withdrawal", money)
            return

        self._balance -= money
        print(f"Withdrew Rs {money}. Remaining balance: Rs {self._balance}")
        self._log("Withdrawal", money)

    def show_balance(self):
        print(f"Current balance: Rs {self._balance}")
        self._log("Checked balance", self._balance)

    def _log(self, action, amount):
        # Protected helper method (internal use only)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("bank_log.txt", "a") as file:
            file.write(f"[{timestamp}] {action}: Rs {amount}\n")


account = BankAccount(5000)   # Creating an object with opening balance

account.show_balance()        # Check balance

account.deposit(2000)         # Deposit money
account.withdraw(1000)        # Withdraw money
account.withdraw(7000)        # Attempt invalid withdrawal

account.show_balance()        # Final balance
