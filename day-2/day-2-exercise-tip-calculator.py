#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percantage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_and_tip = bill
if percentage == 10:
    bill_and_tip = bill * 1.10
elif 12:
    bill_and_tip = bill * 1.12
elif 15: 
    bill_and_tip = bill * 1.15
else:
    bill_and_tipp = False

to_pay = round((bill_and_tip / people), 2)
#also possible to use format() function -> to_pay = "{:.2f}".format(bill_and_tip / people)

print(f"Each person should pay: ${to_pay}")