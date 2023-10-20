two_digit_number = input("Enter two digit number : ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
print(type(two_digit_number))
num = int(two_digit_number)
result = num % 10
result2 = num//10
print("Addition : ", result + result2)
# Another way :
string_num = input("Another Way : Enter two digit number : ")
first_num = string_num[0]
second_num = string_num[1]
print("Addition in diff way : ", int(first_num) + int(second_num))
