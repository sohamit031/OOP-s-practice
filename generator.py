def infinite_counter():
    n = 1
    while True: # This loop never ends!
        yield n
        n += 1

# Create the generator
counter = infinite_counter()

# We can take as much as we want, whenever we want
print(next(counter)) # 1
print(next(counter)) # 2
print(next(counter)) # 3
# ... 10 years later ...
print(next(counter)) # 4
print(next(counter)) # 5
print(next(counter)) # 6
