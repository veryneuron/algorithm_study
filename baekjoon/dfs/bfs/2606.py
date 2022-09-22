from collections import deque

com = int(input())
pair = int(input())
graph = [[] for _ in range(com + 1)]
for _ in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(com + 1)]

dq = deque()
dq.append(1)
visited[1] = True
count = -1

while dq:
    now = dq.popleft()
    count += 1
    for neighbor in graph[now]:
        if visited[neighbor] == False:
            dq.append(neighbor)
            visited[neighbor] = True

print(count)