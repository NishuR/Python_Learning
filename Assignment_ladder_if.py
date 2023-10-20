height = int(input("What is your Height? "))
bill = 0
if height > 120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age < 12:
        bill = bill + 5
        print("your child ticket bill $5")
    elif age <= 18:
        bill = bill + 7
        print("Your youth ticket bill is $7")
    else:
        bill = bill + 12
        print("Your adult ticket bill $12")
    photo = input("Do you want photo? Y and N : ")
    if photo == "Y":
        bill = bill + 3
        print(f"Your final bill is : {bill}")
    else:
        print(f"Your final bill is : {bill}")
else:
    print("Sorry you can not eligible for ride")