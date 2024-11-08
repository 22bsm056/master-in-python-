print("heyu guys how are yoy this is basic calculator where you can perform add sub,mul,divide,reminder")
num=int(input("enter correct operation number for addation:-1,sub:-2,mul:-3,div:-4,remiander:-5 enter here:-"))
a=int(input("enter first digit"))
b=int(input("enter second digit"))
if num==1:
    print(a+b)
elif num==2:
    print(a-b)
elif num==3:
    print(a*b)
elif num==4:
    print(a/b)
elif num==5:
    print(a%b)
else:
    print("please enter correct operation")
print("thank you!! for using me. please visit again")