'''
    linked list is a data structure that has 
        - nodes with a value and a pointer to next node 

    linked list good for 
        - removing item from middle 
        - inserting item in front 

    array is better at 
        - accessing value at specific index (linked list need to traverse down all nodes)
        - easier to program 

'''

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

        # loop until the last item in the list 
        while prevLastNode.next != None: 
            prevLastNode = prevLastNode.next

        lastNode = Node(value,None)

        # point prev last node to last node 
        prevLastNode.next = lastNode


    def addNode(self,value): 

        if (self.head == None): 
            self.addToFront(value)
        elif (value < self.head.value): 
            self.addToFront(value)
        else: 
            tempNode = self.head
            while (tempNode.next != None): 
                if value > tempNode.value and value < tempNode.next.value: 
                    break
                tempNode = tempNode.next

            newNode = Node(value,tempNode.next)
            tempNode.next = newNode


    def removeNode(self,value): 

        tempNode = self.head

        # remove if first 
        if tempNode.value == value: 
            self.head = self.head.next

        # remove middle and last 
        while tempNode != None: 
            if tempNode.next != None and tempNode.next.value == value: 
                break
            tempNode = tempNode.next 

        if tempNode != None: 
            tempNode.next = tempNode.next.next

    # return true if value is found 
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
    myLinkedList.printList() 
    print('-----')
    myLinkedList.addToBack('mark')
    myLinkedList.printList() 

    print('-----')
    myOrderedLL = LinkedList()
    
    # try adding node in different order to test 
    myOrderedLL.addNode('chase')
    myOrderedLL.addNode('amy')  
    myOrderedLL.addNode('sabrina')
    myOrderedLL.removeNode('amy')
    myOrderedLL.printList() 
    print(myOrderedLL.findNode('chase'))
    debug = 1 
