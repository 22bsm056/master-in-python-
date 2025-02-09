num=3453
lst=str(num)
rev=lst[::-1]
print(int(rev))
sum=0
#take three digit from user and add square of them
num=list(map(int,input("enter numbers you want to get addation of square:-").split()))
for i in num:
    sum+=(i**2)
print(sum)