print("welcome to kom banega crorpati yaha aap jeet sakte hai 7 cror always answer full name of your answer as written in option eg: A:ganga then you shoud answer ganga")
kbc=int(input("press 1 to play kbc"))
q1=("what is the captial of india? choose any one answer A:bharat B:patna c:delhi D:goa")
q2=("who is the reachest person in the world?  option A:bill B:adani C:ambani D:elon")
q3=("who is themprime minister of india  A:modi B:nitish C:didi D:pappu")
q4=("total no of IITS in india?  A:10 B:21 C:7 d:0")
q5=("how many states in india?  a:24 ,b:29 c:56 d:67")
q6=("longest river in india? a:GANGA B:yamuna C:tiliya D:bharamputra")
q7=("national father of india?  mera baap B:bappu C:chhacha D:pappu")
q8=("how much gdp of india in 2027?  A:7 B:6 C:5 D:78")
q9=("tcs is a part of which group? a:tesla B:tata C:zomato D:infosys")
q10=("patna is estibilished in the bank of which rever?  A:tiliya B:yamuna C:gomti D:none")
import random
answer=["delhi","elon","modi","21","29","GANGA","bappu","5","tata","none"]
# Define your questions as a list
questions = [q1, q2, q3,q4,q5,q6,q7,q8, q9,q10]

# Select 3 unique questions randomly
random_questions = random.sample(questions, 3)

# Print the selected questions
for question in random_questions:
    while True:
     print(question)
     ans=input("write your answer here")
     if ans in answer:
        print("7 Crorrrrrrrrreeeeeeeeeee ")
        break
else:
        print("padhe ke time tu chatla lad ab harla 7 cror to kahe fatta hako gaad")
    


