lst=[5,6,4,9,3,78,98,34,56,76,89,23,56,78,89]
n=len(lst)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if lst[j]<lst[min_index]:
            min_index=j
    min_value = lst.pop(min_index)
    lst.insert(i, min_value)
print(f"sorted array {lst}")


