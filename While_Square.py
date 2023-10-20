# WAP to find square of x^y number
base = int(input("Enter a digit for base value :"))
power = int((input("Enter the power : ")))
result = 1
while power > 0:
    result = base * result
    power = power - 1
print(result)
