n=int(input("enter your number how many lines of patten you want:-"))
for i in range(1,n+1):
    # print(f" "*(n-i),end="")
    # print(f"*"*((2*i)-1),end="")
    # print("")

    # print(f"*"*i,end="")
    # print("")
    if i==1 or i==(n):
        print(f"*"*n,end="")
        print("")
    else:
        print(f"*"," "*(n-4),"*",end="")
        print("")
