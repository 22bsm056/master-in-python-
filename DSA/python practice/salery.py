def unique(arr):
    out=[]
    for i in range (len(arr)):
        for j in range (len(arr)):
            txt=str(arr[i]) + str(arr[j])
            if txt not in out:
                out.append(txt)
    return out
arr=list(map(int,input("enter space seprated value:-").split()))
#arr=list(map(int,input("list the element with space seprated:-").split()))
print(f"unique combinations are:-{unique(arr)}")

