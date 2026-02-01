# --- THE GENERATOR FUNCTION ---
def get_numbers_gen():
    print("⚡ Generator starting...")
    yield 24
    print("...Pausing...")
    yield 2
    print("...Pausing...")
    yield 3
    print("✅ Done!")

# --- HOW TO RUN IT ---

# 1. Create the generator object (It starts paused)
my_gen = get_numbers_gen()
print(f"Status: {my_gen}") 

# 2. Manually press "Play" (next) to get values one by one
print("\n--- Pulling 1st Value ---")
val1 = next(my_gen)
print(f"Received: {val1}")

print("\n--- Pulling 2nd Value ---")
val2 = next(my_gen)
print(f"Received: {val2}")

print("\n--- Pulling 3rd Value ---")
val3 = next(my_gen)
print(f"Received: {val3}")