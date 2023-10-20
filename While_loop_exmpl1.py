# WAP to print factorial of a number 1*2*3*4....n
num = int(input("Enter a number for factorial :"))
fact = 1
while num > 0:
    fact = fact * num
    num = num - 1
print("Factorial :", fact)
