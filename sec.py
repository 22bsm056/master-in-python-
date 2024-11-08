
#Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language
import random
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decodeName=int(input("text here for secure chat:-"))
name=input("text here for secure chat")
rand="abcdefghijklmnopqrstuvwxyz"
def sec(name):
    if len(name)<3:
        rname=name.reverse()
    else:
        x=name[1:]
        y=(x+name[0])
        xy=random.sample(rand,6)
        final=((xy[:2])+y+(xy[3:5]))
        return sec(name)




    