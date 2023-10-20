# Which year do you want to check?
year = int(input("Put a Year to check : "))
# Write your code below this line 👇
if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year")



