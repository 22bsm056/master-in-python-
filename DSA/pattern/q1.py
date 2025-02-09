#my code 
for i in range(4):
    print("*"*4,end=" ")
    print()

    #tutorial code
for i in range(4):
    print(''.join(['*' for _ in range(4)]), end=" \n")

i = 0
while i < 4:
    print("*" * 4, end=" \n")
    i += 1


[print("*" * 4, end=" \n") for _ in range(4)]

list(map(lambda _: print("*" * 4, end=" \n"), range(4)))


for i in range(4):
    print("{}".format("*" * 4), end=" \n")
