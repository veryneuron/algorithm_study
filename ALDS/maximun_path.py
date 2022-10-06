import sys

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N):
    source, dest, weight = map(int, input().split())
    graph[source].append((dest, weight))

result_path = []
result_weight = 0

def dfs(edge, visited, weight_sum):
    to_A_weight = -sys.maxsize
    max_weight_edge = -1
    max_weight = -sys.maxsize
    for d, w in graph[edge]:
        if d == 0:
            to_A_weight = w
        if w > max_weight and d not in visited:
            max_weight = w
            max_weight_edge = d
    if weight_sum + to_A_weight > result_weight and len(visited) > 1:
        result_weight = weight_sum + to_A_weight
        result_path = [*visited, 0]
    
    if max_weight_edge != -1:
        dfs(max_weight_edge, [*visited, max_weight_edge], weight_sum + max_weight)
    
dfs(0, [0], 0)
print(*result_path, sep='->')
print(result_weight)