# Write a program that adds the digits in a 2digit number. e.g. if the input was 35,
# then the output should be 3 + 5 = 8
# Warning. Do not change the code on line 1.
# Your program should work for different inputs. e.g. any two-digit number.
two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
num = int(two_digit_number)
result = num % 10
result2 = num//10
print(result + result2)

#-------------------------------------------Another Way

first_num = int(two_digit_number[0])
second_num = int(two_digit_number[1])
print(first_num + second_num)



