# Tip-calculator
print("Welcome to Tip calculator!")
bill = float(input("What was the total bill :₹"))
tip = int(input("How much tip would you like to give ? 10,12,15? : "))
people= int(input("Enter number of people: "))
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person,2) 
print(f"each person should pay : ₹{final_amount}, and total bill is ₹{round(total_bill,2)}")
