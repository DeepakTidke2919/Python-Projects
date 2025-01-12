print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0


if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age"))
    if age <= 8:
        bill = 5
        print("Please pay 5$")
    elif age <= 14:
        bill = 7
        print("Please pay 7$")
    else:
        bill = 10
        print("Please pay 10$")

    Want_Photo = input("If you want photo taken Tipe Y for yes and N for No")

    if Want_Photo == "Y":
        bill += 3
        print(f"Your Final Bill is {bill}")
    else:
        print(f"Your final Bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
