import random
names = ["nishu", "rohit", "rishu", "rajni"]
print(type(names))
random_number = random.randint(0, len(names)-1)
final = names[random_number]
print(f"{final} is going to buy the meal today! ")
