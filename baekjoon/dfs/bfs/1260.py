# 탐색 프로그램, dfs 순서대로, bfs 순서대로 출력, 정점 번호 작은 거 우선
# 두 정점 사이 간선 여러 개 있을 수 있음, 양방향

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited_dfs = [False for _ in range(N+1)]
result_dfs = []
def dfs(edge):
    result_dfs.append(edge)
    visited_dfs[edge] = True
    for neighbor in sorted(graph[edge]):
        if visited_dfs[neighbor] == False:
            dfs(neighbor)
visited_bfs = [False for _ in range(N+1)]
result_bfs = []
def bfs(start):
    dq = deque()
    dq.append(start)
    visited_bfs[start] = True
    while dq:
        now = dq.popleft()
        visited_bfs[now] = True
        result_bfs.append(now)
        for neighbor in sorted(graph[now]):
            if visited_bfs[neighbor] == False:
                dq.append(neighbor)
                visited_bfs[neighbor] = True
dfs(V)
bfs(V)
print(*result_dfs)
print(*result_bfs)