print(" ************** Welcome to the Roller coaster Ride ********* "
      " \n *********************************************************** ")


Person_Age = int(input("Please enter your age"))

print(f"Your age is: {Person_Age}")

Person_Height = int(input("Please enter your height"))

print(f"Your height is {Person_Height}")


if Person_Height >= 100:
    print("You are allow to ride Roller Coaster :) ")
    if Person_Age <= 12:
        print("Please pay 10$ for Ticket")
    elif Person_Age <=18:
        print("Please pay 15$ for Ticket")
    else:
        print("Please pay 20$ for Ticket")

else:
    print("Sorry, you cannot ride the Roller Coaster, Better luck next time :( ")