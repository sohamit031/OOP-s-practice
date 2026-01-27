class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        # We assume the initial price is valid, or we could use the setter here too
        self.__price = price 

    # GETTER
    def get_price(self):
        return self.__price

    # SETTER
    def set_price(self, new_price):
        # The Guard Logic
        if new_price > 0:
            self.__price = new_price
            print(f"Price updated to ${self.__price}")
        else:
            print("Failed: Price cannot be negative or zero.")

# --- Testing ---
my_phone = Phone("iPhone", 999)

# Scenario A: The intern tries to set the price to -500
my_phone.set_price(-500)
# Output: Failed: Price cannot be negative or zero.

# Scenario B: The manager sets the price to 899
my_phone.set_price(899)
# Output: Price updated to $899

# Scenario C: Trying to hack the variable directly
# print(my_phone.__price)
# Output: AttributeError: 'Phone' object has no attribute '__price'