# Create a program using maths and f-Strings that tells us
# how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
age_int = int(age)
expected_age = 90 - age_int
x = expected_age * 52
print(f"You have {x} weeks left.")