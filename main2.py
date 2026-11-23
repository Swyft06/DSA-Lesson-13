from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def AddEdge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v)

        for neighbors in self.graph[v]:
            if neighbors not in visited:
                self.DFSUtil(neighbors,visited)

    def DFS(self,v):
        visited = set()
        self.DFSUtil(v,visited)

g = Graph()
g.AddEdge(0,1)
g.AddEdge(0,2)
g.AddEdge(1,2)
g.AddEdge(2,0)
g.AddEdge(2,3)

print("DFS: ")
g.DFS(0)
