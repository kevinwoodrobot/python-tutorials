'''
    naming KWQueue since queue module exist

    first in, first out 
    breath first search 
'''
class KWQueue: 
    def __init__(self):
        self.queue = []

    def enqueue(self,data): 
        self.queue.append(data)

    def dequeue(self): 
        return self.queue.pop(0)

    def isEmpty(self): 
        return len(self.queue) == 0

    def getFront(self): 
        return self.queue[0]

    def printQueue(self): 
        for i in range(len(self.queue)): 
            print(self.queue[i])

myQueue = KWQueue() 
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.printQueue() 
print('getFront:',myQueue.getFront())
myQueue.dequeue()
myQueue.printQueue() 

