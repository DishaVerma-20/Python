# Depth First Search
class Graph:
    def __init__(self, vertex):
        self.mat = [[0]*vertex for x in range(vertex)]
        self.size = vertex

    def add_edge(self, src, dest):
        if (0 <= src < self.size and 0 <= dest < self.size):

            # undirected graph
            self.mat[src][dest] = 1
            self.mat[dest][src] = 1

            # directed graph
            # self.mat[src][dest] = 1

    def add_edge_weighted(self, src, dest, weight):
        if (0<=src<self.size and 0<=dest<self.size):
            self.mat[src][dest] = weight
            self.mat[dest][src] = weight
        else:
            print("Invalid edge")
        
    def print(self):
        for row in self.mat:
            print(' '.join(map(str, row)))

    def dfs(self, src):
        visited = [False]*self.size
        stack = [src] # list mai inbuilt push pop hota haii

        while stack: # mtlb jbtk stack empty nahi ho jaata haii
            v = stack.pop()

            if visited[v]==False: # abhi tk visit nahi kiya haii
                print(v, end = ' ')
                visited[v] = True

            for i in range(self.size): # particular node se connected elements stack maii
                if self.mat[v][i] == 1 and visited[i] == False:
                    stack.append(i) # elemnts push ho jaayge, main kaam krega pop

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.dfs(0)
