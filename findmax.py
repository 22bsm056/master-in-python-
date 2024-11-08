n=int(input("enter your first age "))
n2=int(input("enter your 2nd age "))
n3=int(input("enter your 3rd age "))
if n2<n>n3:
    print(f"older age is {n}")
elif n<n2>n3:
    print(f"older age is {n2}")
else:
    print(f"older age is {n3}")

#use this print(max(n,n2,n3))