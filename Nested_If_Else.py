# WAP for Roller Coaster eligibility criteria
print("Welcome to the Roller Coaster!!")
height = int(input("Enter the height in cm? : "))
if height > 120:
    print("Yes you can ride the roller coaster.")
    age = int(input("Enter the age? :"))
    if age < 12:
        print("Ride fee : $5")
    elif age <= 18:
        print("Ride fee : $7")
    else:
        print("Ride fee : $12")
else:
    print("Sorry, you have to grow taller before you can ride.")

