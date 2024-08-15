print("Welcome to the tip calculator!")

totalBill = float(input("How much was your bill? "))
totalTip = int(input("How much would you like to tip? 10, 12, or 15 percent? "))
totalPeople = int(input("How many people are splitting the bill? "))

splitBill = (totalBill + (totalBill * (totalTip / 100))) / totalPeople

print(f"Each person should pay: ${round(splitBill, 2)}")