print("******Welcome to Python Pizza Deliveries!******")

bill = 0

size = input("What size pizza do you want? S, M or L: ")

if size == "S":
    bill = 15
    print("Your bill is 15$")

elif size == "M":
    bill = 20
    print("Your bill is 20$")

else:
    bill = 25
    print("Your bill is 25$")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

if size == "S" and pepperoni == "Y":
    bill += 2
    print(f"***Your bill with pepperoni***: {bill}$")
elif pepperoni == "Y":
    bill += 5
    print(f"Your final bill is: {bill}$")

else:
    print(f"Your bill is: {bill}$")

extra_cheese = input("Do you want extra cheese? Y or N: ")

if extra_cheese == "Y":
    bill += 2
    print(f"Your final bill is:**** {bill}$")
else:
    print(f"Your Final bill is:****{bill}$")

