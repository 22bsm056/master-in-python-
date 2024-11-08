class stack:
    def __init__(self):
        self.stack=[]
    #push
    def push(self,elem):
        self.stack.append(elem)
    def pop(self):
        if self.isempty():
            return "stack is empty"
        return self.stack.pop()
    #peek
    def peek(self):
        if self.isempty():
            return"stack is empty"
        return self.stack[-1]
    def isempty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)

myStack = stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')
print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isempty())

print("Size: ", myStack.size())