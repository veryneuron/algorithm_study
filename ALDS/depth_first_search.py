# depth first search implementation
#
# implementation by using recursion

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, v):
        visited = [False for _ in range(max(self.graph) + 1)]
        self.visit_dfs(v, visited)

    def visit_dfs(self, cur, visited):
        visited[cur] = True
        print(cur, end=' ')
        for i in self.graph[cur]:
            if visited[i] == False:
                self.visit_dfs(i, visited)

# Driver code

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)