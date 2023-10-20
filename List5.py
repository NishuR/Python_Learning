li = [65, 10, 259, 13, 18, 66, 36]
minvalue = li[0]
maxvalue = li[0]
for i in li:
    if i > maxvalue:
        maxvalue = i
    elif minvalue > i:
        minvalue = i
print("Minimum Value : ", minvalue)
print("Maximum value : ", maxvalue)
