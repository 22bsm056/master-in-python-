my_list=[17,3,44,56,23,45,78,54,78]
largest=my_list[0]
for i in range(1,len(my_list)):
    if my_list[i]>largest:
        largest=my_list[i]
print(largest)