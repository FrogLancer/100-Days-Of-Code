# Day 2, Tip Calculator


print("Welcome to the tip calculator.")

totalBill = float(input("What is the total bill?: "))
numPeople = int(input("How many people to split the bill?: "))
percentTip = float(input("What percentage would you like to tip?: "))

billWithTip = totalBill + (totalBill * (percentTip / 100))
eachToPay = round(billWithTip / numPeople, 2)

print(f"Each person should pay: {eachToPay}")

#    pemdas
