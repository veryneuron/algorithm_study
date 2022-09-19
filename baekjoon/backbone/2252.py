# 위상 정렬

# 코드 참고
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

q = deque()
result = []

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            q.append(i)

print(*result)
