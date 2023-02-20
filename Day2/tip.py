import math
print("TIP CALCULATOR")
total_bill = float(input("What is the total bill amount: "))
tip_percentage = float(input("What tip percentage would you like to give? (please choose between 10, 12, 15): "))
people = int(input("How many people will split the bill!"))

tip = total_bill * (tip_percentage * .01 )
total = total_bill + tip
pay = round((total / people), 2)

print(f"Each person will pay: {pay}")