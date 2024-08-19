import random

random_integer = random.randint(1, 10)

print(random_integer)

# Coin Flipper

result = random.randint(0, 1)

if result == 0:
    print("Heads")
if result == 1:
    print("Tails")


# Random Element from a List

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

selected_friend = random.randint(0, 4)

print(friends[selected_friend])

# Alternative solution

print(random.choice(friends))