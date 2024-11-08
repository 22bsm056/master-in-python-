def rathouse(r,unit,arr):
    if arr is None or len(arr)==0:
        return -1
    tof=r*unit
    fnow=0
    for house in range(len(arr)):
        fnow += arr[house]
        if fnow >=tof:
            return house +1
    return 0
r=int(input("enter number of rats:-"))
unit=int(input("enter value of unit:-"))
arr=list(map(int,input("list the element with space seprated:-").split()))
result=rathouse(r,unit,arr)
print(result)


      

        
