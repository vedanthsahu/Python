def deposit(self, money):
    """Add money to balance only if amount is positive."""
    
    # Block invalid deposit
    if money <= 0:
        print("Invalid deposit amount")
        self._log(f"WARNING: Attempted invalid deposit amount: {money}")
        return

    # Valid deposit
    self.amount += money
    print(f"Deposited Rs {money}. Updated Balance Rs {self.amount}")
    self._log(f"Deposited Rs {money}. New balance Rs {self.amount}")
