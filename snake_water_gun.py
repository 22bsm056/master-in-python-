import random
computerint=random.choice([1, 2, 3])
youint=int(input("enter your choice 1:snake ,2:water ,3:gun:-"))
data={1:"snake",2:"water",3:"gun"}
#rdata={"snake":1,"water":2,"gun":3}
com=data[computerint]
you=data[youint]
print(f"your choice is  {you} and computer choice is {com}")
if you==com:
    print("game draw play again")
elif you=="snake" and com=="water":
    print("you lost")
elif you=="snake" and com=="gun":
    print("you lost")
elif you=="water" and com=="snake":
    print("you won")
elif you=="water" and com=="gun":
    print("you won")
elif you=="gun" and com=="snake":
    print("you won")
elif you=="gun" and com=="water":
    print("you lost")
else:
    print("please enter valid choice ")
print("thank you for playing please visit again")
print(com)