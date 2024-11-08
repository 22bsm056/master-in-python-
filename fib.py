n=int(input("enter number to find fibbonachi"))
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+n)
print(fib(n))