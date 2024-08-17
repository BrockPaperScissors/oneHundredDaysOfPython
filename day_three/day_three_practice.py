# odd/even checker
# user_input = int(input("Enter a number: "))
#
# if user_input % 2 == 0:
#     print("input was even")
# else:
#     print("input was odd")


# Pizza Deliveries Exercise -- else/if/logic operator practice
print("Welcome to Pizza Deliveries")
pizza_size = input("What size pizza would you like? Small, Medium, or Large: ").lower()
pepperoni = input("Do you want to add pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Would you like extra cheese? Y or N: ").lower()
bill = 0


if pizza_size == "small":
    bill += 15
elif pizza_size == "medium":
    bill += 20
elif pizza_size == "large":
    bill += 25
else:
    print("Please enter a valid size.")

if extra_cheese == "y":
    bill += 1
if pepperoni == "y" and pizza_size == "medium" or pizza_size == "large":
    bill += 3
elif pizza_size == "small":
    bill += 2

print(f"Your total will be ${bill},")


