class Node: 
    def __init__(self,value,next): 
        self.value = value 
        self.next = next 

class LinkedList: 
    def __init__(self): 
        self.head = None 

    def printList(self): 
        tempNode = self.head 
        while tempNode != None: 
            print(tempNode.value)
            tempNode = tempNode.next 

    def addToFront(self,value): 
        tempNode = Node(value,self.head)
        self.head = tempNode 

    def addToBack(self,value): 
        prevLastNode = self.head 

        while prevLastNode.next != None: 
            prevLastNode = prevLastNode.next 

        lastNode = Node(value,None)
        prevLastNode.next = lastNode 

    def addNode(self,value): 
        if(self.head == None): 
            self.addToFront(value)
        elif (value < self.head.value): 
            self.addToFront(value)
        else: 
            tempNode = self.head 
            while (tempNode.next != None): 
                if (value > tempNode.value and value < tempNode.next.value): 
                    break 
                tempNode = tempNode.next 
            
            newNode = Node(value,tempNode.next)
            tempNode.next = newNode 

    def removeNode(self,value): 
        tempNode = self.head 

        if tempNode.value == value: 
            self.head = self.head.next 

        while tempNode != None: 
            if tempNode.next != None and tempNode.next.value == value: 
                break 
            tempNode = tempNode.next 

        if tempNode != None: 
            tempNode.next = tempNode.next.next 

    def findNode(self,value): 
        tempNode = self.head 
        while tempNode != None: 
            if tempNode.value == value:
                return True
            tempNode = tempNode.next 

        return False 

if __name__ == "__main__": 
    myLinkedList = LinkedList()
    myLinkedList.addToFront('kevin')
    myLinkedList.addToFront('john')
    myLinkedList.addToBack('gary')
    myLinkedList.printList()

    print('-----------')

    myOrderedLL = LinkedList() 
    myOrderedLL.addNode('kevin')
    myOrderedLL.addNode('amy')
    myOrderedLL.addNode('sabrina')
    myOrderedLL.removeNode('kevin')
    myOrderedLL.printList()
    print(myOrderedLL.findNode('kevin'))
