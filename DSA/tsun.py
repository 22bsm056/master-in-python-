#brute force
lst=[2,6,5,8,11]
tg=14
for l in range(len(lst)):
    for j in range(len(lst)):
        if (lst[l]+lst[j])==tg:
            print("yes")
            break