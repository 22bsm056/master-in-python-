stack=[]
stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
print(f"stack is {stack}")
#pop
el=stack.pop()
print(f"removed element is {el}")
#peek
te=stack[-1]
print(f"top element is {te}")
#isempty
isEmpty=not bool (stack)
print(f"isempty{isEmpty}")
#siz3
print(len(stack))