class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        print(f"Withdrawal successful. New Balance: ${self.balance}")

# --- STEP 1: LOAD DATA (Read from file) ---
filename = "balance.txt"
current_balance = 0

try:
    # Try to open the file to read the old balance
    with open(filename, "r") as f:
        data = f.read()
        current_balance = float(data) # Convert text "100" to number 100.0
        print(f"Welcome back! Loaded balance: ${current_balance}")

except FileNotFoundError:
    # If file doesn't exist (first time running), start with default
    current_balance = 1000.0
    print("No previous account found. Creating new account with $1000.")

# --- STEP 2: PERFORM OPERATION ---
my_atm = ATM(current_balance)

amount_to_take = float(input("How much do you want to withdraw? "))

try:
    my_atm.withdraw(amount_to_take)
except ValueError as e:
    print(f"Error: {e}")

# --- STEP 3: SAVE DATA (Write to file) ---
# We overwrite the file with the NEW balance
with open(filename, "w") as f:
    f.write(str(my_atm.balance)) # Must convert number back to string to write it
    print("Balance saved successfully!")