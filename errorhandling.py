class ATM:
    def __init__(self, balance):
        self.balance = balance

    # THIS is the method you asked for
    def withdraw(self, amount):
        # Step 1: The Logic Check
        if amount > self.balance:
            # Step 2: Raise the error manually
            raise ValueError("Insufficient Funds! You don't have enough money.")
        
        # Step 3: If no error, proceed normally
        self.balance = self.balance - amount
        print(f"Success! Remaining balance: ${self.balance}")

my_atm=ATM(100)

try:
    my_atm.withdraw(50)

except ValueError as e :
    print(f"transaction failed: {e}") 