class Graph:
    def __init__(self):
        self.adjList = {} 

    def add_vertex(self, vertex):
        if vertex not in self.adjList: # gives the list of all the keys
            self.adjList[vertex] = []

    def add_edge(self, src, dest):
        self.add_vertex(src) # ony if directed graph
        self.add_vertex(dest) # koi dikkt nhi, kyuki condition is there

        self.adjList[src].append(dest) # directed graph ka kaam ho gaya
        self.adjList[dest].append(src) # undirected graph hai nh

    def printGraph(self):
        for vertex in self.adjList:
            print(vertex , " --> ", self.adjList[vertex], end = '\n') # particular key se connected saare elements return ho jayge

g = Graph()
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(4,5)
g.add_edge(3,5)
g.add_edge(4,3)

g.printGraph()