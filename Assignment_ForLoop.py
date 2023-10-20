# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
add = 0
for i in student_heights:
    add = add + i
print(f"addition of student heights : {add}")
counting = 0
for i in student_heights:
    counting =+ 1
print(f"number of students : {counting}")
average_height = add / counting
print(f" Average of students height  = {average_height}")



