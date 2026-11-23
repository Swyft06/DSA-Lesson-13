#dfs - depths first search

graph = {
    'A':['B','C','D'],
    'B':['E'],
    'C':['D','E'],
    'D':[],
    'E':[]
}

l = [1,3,5,7,1,2,7]
print(l)

var1 = set(l)
print(var1)

visited = set()

def dfs(visited,graph,root):
    if root not in visited:
        print(root)

        visited.add(root)

        for neighbor in graph[root]:
            dfs(visited,graph,neighbor)

dfs(visited,graph,'A')