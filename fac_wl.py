try:
 n=int(input("enter number to get factorials"))
 def fac(n):
  if n==0 or n==1:
    return 1
  else:
    return n*(fac(n-1))
 print("factorial of given number is:-",fac(n))
except:
  print("sorry for inconvience")


