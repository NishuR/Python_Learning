# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# Which number do you want to check?
number = int(input("Enter a number : "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
