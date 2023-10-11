'''
    data structure 
        last in, first out
    good for 
        depth first search 

'''
class Stack: 
    def __init__(self): 
        self.stack = [] 

    def push(self,data): 
        self.stack.append(data)

    def pop(self): 
        return self.stack.pop()

    def isEmpty(self): 
        return len(self.stack) == 0
      
    def getTop(self): 
        return self.stack[-1]

    def print(self): 
        for i in range(len(self.stack)): 
            print(self.stack[i])

if __name__ == '__main__': 
    myStack = Stack() 
    myStack.push(1)
    myStack.push(2)
    myStack.print()
    print(myStack.getTop())
    print('---------------')
    myStack.pop()
    myStack.print()
    print(myStack.isEmpty())
 
