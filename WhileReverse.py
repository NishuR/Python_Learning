# Write a program to print reverse of a number like : 123 - 321
n = int(input("Put any number for reverse : "))
result = 0
rem = 1
while n > 0:
    rem = n % 10
    result = result * 10 +rem
    n = n // 10
print(result, end=" ")
