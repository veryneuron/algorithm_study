# breadth_first_search implementation
#
# implementation by using deque(queue)
# code from geeksforgeeks
from collections import defaultdict, deque

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False for x in range(max(self.graph) + 1)]
        de = deque()
        de.append(s)
        visited[s] = True

        while de:
            temp = de.popleft()
            print (temp, end = " ")
            for i in self.graph[temp]:
                if visited[i] == False:
                    de.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)