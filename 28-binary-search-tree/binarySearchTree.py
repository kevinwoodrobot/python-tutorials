'''
    tree structure
        sorting is usually nlog(n)

    binary search tree follows ORDER 
    binary tree does not follow order 


    different traversal methods 
        1. pre order - process current node and then left and right sub trees 
        2. in order - process tree in order 
        3. post order - process left and right sub trees before current node 
        4. level order - visit each level of the tree


'''
class Node:
    def __init__ (self,value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree: 
    def __init__(self): 
        self.root = None

    def insert(self,value): 
        if self.root == None: 
            self.root = Node(value)
            return 

        cur = self.root

        while True: 
            if value == cur.value: 
                return
            if value < cur.value: 
                if cur.left != None: 
                    cur = cur.left
                else: 
                    cur.left = Node(value)
                    return 
            elif value > cur.value: 
                if cur.right != None: 
                    cur = cur.right
                else: 
                    cur.right = Node(value)
                    return

    def inOrderPrint(self,curNode): 
        if curNode == None: 
            return 
        self.inOrderPrint(curNode.left)
        print(curNode.value)
        self.inOrderPrint(curNode.right)

    def find(self,value,curNode): 
        if curNode == None: 
            return False
        elif value == curNode.value: 
            return True
        elif value < curNode.value: 
            return self.find(value,curNode.left)
        else: 
            return self.find(value,curNode.right)

    def findMin(self,curNode): 
        if curNode == None: 
            return None 
        
        while curNode.left != None: 
            curNode = curNode.left 

        return curNode.value

    def findMax(self,curNode): 
        if curNode == None: 
            return None 
        
        while curNode.right != None: 
            curNode = curNode.right 

        return curNode.value

if __name__ == '__main__': 
    myTree = BinarySearchTree() 
    myTree.insert('kevin')
    myTree.insert('amy')
    myTree.insert('yolo')
    myTree.inOrderPrint(myTree.root) 
    print(myTree.find('john',myTree.root))
    print('min:',myTree.findMin(myTree.root))
    print('max:',myTree.findMax(myTree.root))