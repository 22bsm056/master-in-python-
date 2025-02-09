#M1 by using simple method 
edge=[5,7,9]
max1=max(edge)
print(max1)

#m2 find unique number of letter in string
str="ffuckyouubabyyy"
lst=set(str)
print(len(lst))


#m3 use sort method to do this 
edge=[8,9,45,67,23,89]
edge.sort(reverse=True)
print(edge[0])

#m4 do it again with string
edge=list(map(int,input("enter edge seprated by space").split()))
print(max(edge))

#using sort method 
#edges = list(map(int, input("Enter 5 edges separated by spaces: ").split()))
edge.sort()
print("The largest edge is:", edge[-1])

#using loop
me=edge[0]
for i in edge:
    if me<i:
        me=i
print(me)

max1=sorted(edge)[-1]
print(max1)