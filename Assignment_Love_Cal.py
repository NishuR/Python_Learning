print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combine_name = name1 + name2
lowercase = combine_name.lower()
t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
first_digit = t + r + u + e
l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score <= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
