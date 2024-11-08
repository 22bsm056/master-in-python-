my_array=[23,45,64,87,34,23,4,6,7,8,5,7,3,5,6,9,89,65]
n=len(my_array)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if my_array[j]<my_array[min_index]:
            min_index=j
    my_array[i],my_array[min_index]=my_array[min_index],my_array[i]
print(f"sorted list is {my_array}")