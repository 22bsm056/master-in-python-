array=[6,5,7,8,9,3,5,6,78,98,45,34,67,56,78,87]
for i in range(len(array)-1):
    for j in range(len(array)-i-1):
        if array[j]<array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(f"shorted array is {array}")