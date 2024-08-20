import random

# Declare what we can use in our password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '@', '$', '%', '&', '(', '*', ')', '+']

# Store all of our options in a single list

# options = [letters, numbers, symbols]

# Get the desired length of password from the user

# letter_count = int(input("How many letters would you like in your password? "))
# symbol_count = int(input("How many symbols would you like in your password? "))
# number_count = int(input("How many numbers would you like in your password? "))
# total_length = letter_count + symbol_count + number_count
#
# print(total_length)

# new_password = ""


# Attempting to brute force it without using .choice -- generates random password but stuck trying to factor in
#   specific number of letters/nums/symbols

# for x in range(total_length):
#     random_category = random.randrange(0, 3)
#     current_list_size = len(options[random_category])
#     char_value = random.randrange(0, current_list_size)
#     new_password += str(options[random_category][char_value])
#
# print(new_password)

letter_count = int(input("How many letters would you like in your password? "))
number_count = int(input("How many numbers would you like in your password? "))
symbol_count = int(input("How many symbols would you like in your password? "))

new_pass = ""
password_list = []

for x in range(0, letter_count):
    make_upper = random.randint(0, 1)
    letter = random.choice(letters)

    if make_upper == 0:
        password_list.append(letter.upper())
    else:
        password_list.append(letter)



for x in range(0, number_count):
    password_list.append(random.choice(numbers))
for x in range(0, symbol_count):
    password_list.append(random.choice(symbols))


print(password_list)
random.shuffle(password_list)
print(password_list)

for x in range(0, len(password_list)):
    new_pass += password_list[x]

print(f"Your new password is {new_pass}")



