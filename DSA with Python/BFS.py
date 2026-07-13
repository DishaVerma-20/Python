# Breadth First Search
from collections import deque

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
        
    def BFS(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True

        while (queue):
            # or while (queue != None), dono se kuch bhi chlega
            v = queue.popleft()
            print(v, end = ' ')

            for i in range(self.size): # o se size se 1 km tak chlega, if size is 8, then 7 tak
                if (self.mat[v][i] == 1 and visited[i] == False):
                    visited[i] = True
                    queue.append(i)

g = Graph(8)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(1, 3)
g.add_edge(3, 5)
g.add_edge(3, 4)
g.add_edge(5, 4)
g.add_edge(4, 6)
g.add_edge(6, 2)
g.add_edge(6, 7)
g.BFS(0) # starting node is 0