# 1. NORMAL FUNCTION (The DVD)
def get_numbers_list():
    numbers = []
    print("📦 Building the big list...")
    for i in range(1, 4):
        numbers.append(i)
    return numbers  # Sends back the WHOLE list at once

# 2. GENERATOR (The Stream)
def get_numbers_gen():
    print("⚡ Generator starting...")
    yield 1
    print("...Pausing...")
    yield 2
    print("...Pausing...")
    yield 3
    print("✅ Done!")

# --- EXECUTION ---

print("--- 1. LIST ---")
my_list = get_numbers_list()
print(my_list)

print("\n--- 2. GENERATOR ---")
my_gen = get_numbers_gen()
print(my_gen) # Notice: It doesn't print numbers yet! It prints a "generator object"

print("\n--- PULLING VALUES ---")
# We have to ask for the items one by one
print(next(my_gen)) 
print(next(my_gen))
print(next(my_gen))



