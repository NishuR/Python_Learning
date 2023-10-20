li = [65, 10, 259, 13, 18, 66, 36]
even = []
odd = []
for i in li:
    if i % 2 == 0:
        even = even + [i]
    elif i % 2 != 0:
        odd = odd + [i]
print(even)
print(odd)
