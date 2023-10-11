'''
    graph implementation using adjacency list 
    another way is to use adjacency matrix (2d matrix)

    similar to how facebook works
'''
class Graph: 
    def __init__(self): 
        # make empty dictionary to hold the graph 
        self.graph = {} 

    def addVertex(self,vertex): 
        # assume repeated vertices are ok for now 
        # initialize empty list of edges for each vertex 
        self.graph[vertex] = []

    def addEdge(self,v1,v2): 
        # add vertex to list of edges for v1 and v2
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    def printGraph(self): 
        for key, value in self.graph.items(): 
            print(f"{key}: {value}")

    def removeVertex(self,vertex): 
        if vertex not in self.graph: 
            return "Invalid vertex"

        del self.graph[vertex]

        for key, value in self.graph.items(): 
            if vertex in value: 
                value.remove(vertex) 
    
    def getVertices(self): 
        return list(self.graph.keys())

    def getEdges(self,vertex): 
        return self.graph[vertex]

if __name__ == '__main__': 
    myGraph = Graph() 
    myGraph.addVertex(1)
    myGraph.addVertex(2)
    myGraph.addVertex(3)
    myGraph.addEdge(1,2)
    myGraph.addEdge(2,3)
    myGraph.addEdge(1,3)
    myGraph.printGraph() 
    print('vertices:',myGraph.getVertices())
    print('edges for vertex 1:',myGraph.getEdges(1))
    myGraph.removeVertex(3)
    print('------------------')
    myGraph.printGraph() 
    debug = 1 
