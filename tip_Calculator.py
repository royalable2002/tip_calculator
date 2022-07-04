print("Welcome to TIP CALCULATOR !!!")

bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_tip = (tip / 100) * bill
total_bill = bill + total_tip

people_share = total_bill / people

message = "{:.2f}".format(people_share)

print(f"Ech person should pay : {message}")


