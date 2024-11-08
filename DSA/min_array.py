data=[6,7,9,4,5,3,98,23,45,67,23,78,90]
minval=data[0]
for i in data:
    if minval>i:
        minval=i
    else:
        pass
print(f"min value is {minval}")
