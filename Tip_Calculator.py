print("*********Welcome to the tip calculator**********")

total_Number_peopel = int(input("How many total number of peopel: "))

print(total_Number_peopel)

Tip_Give = int(input("How much tip you want to give, 10 20 30: "))

print(Tip_Give)

Total_bill = int(input("Total bill of all persons"))

print(Total_bill)

Bill_Each_Person = (Total_bill + Tip_Give)  / total_Number_peopel

print(Bill_Each_Person)