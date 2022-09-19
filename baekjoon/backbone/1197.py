# 최소 신장 트리

import sys
import heapq

input = sys.stdin.readline

# prim - 최소값 찾는거를 heapq로 해야 시간이 맞음, weight가 앞으로 가야 heap정렬이 됨

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    source, goal, weight = map(int, input().split())
    graph[source].append((weight, goal))
    graph[goal].append((weight, source))

visited = set()
pq = [(0, 1)]
total_weight = 0
count = 0

while count < V:
    w, g = heapq.heappop(pq)
    if g not in visited:
        visited.add(g)
        total_weight += w
        count += 1
        for i in graph[g]:
            if i[1] not in visited:
                heapq.heappush(pq, i)

print(total_weight)

# kruskal - cycle 체크시 union find 사용

input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
root = list(range(V + 1))
rank = [0] * (V + 1)
for _ in range(E):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: x[2])

total_weight = 0

def find(x):
    if root[x] == x:
        return x
    return find(root[x])

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if rank[x_root] < rank[y_root]:
        root[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        root[y_root] = x_root
    else:
        root[y_root] = x_root
        rank[x_root] += 1

# union find부분 rank 없이 최적화하기
# def find(a):
#     if a != parent[a]:
#         parent[a] = find(parent[a])
#     return parent[a]


# def union(a, b):
#     a = find(a)
#     b = find(b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a

for source, goal, weight in graph:
    if find(source) != find(goal):
        union(source, goal)
        total_weight += weight

print(total_weight)



# hackerrank 성공, 백준 실패 - 아마 상수항 복잡도 문제? 우선순위 큐 사용필요

# visited = set()
# set.add(1)
# total_weight = 0

# for _ in range(V-1):
#     minimum = (0, 0, sys.maxsize)
#     for i in visited:
#         for g in graph[i]:
#             if g[1] not in visited:
#                 minimum = min(minimum, g, key=lambda x: x[2])
#     visited.add(minimum[1])
#     total_weight += minimum[2]

# print(total_weight)

# prim adj matrix <- 메모리 초과!!

# input = sys.stdin.readline

# V, E = map(int, input().split())
# graph = [[sys.maxsize]*V for _ in range(V)]
# for _ in range(E):
#     s, g, weight = map(int, input().split())
#     graph[s-1][g-1] = min(weight, graph[s-1][g-1])

# selected_node = [0] * V

# no_edge = 0
# selected_node[0] = True
# total_weight = 0
# a = 0
# b = 0

# while (no_edge < V - 1):
#     minimum = sys.maxsize
#     a = 0
#     b = 0
#     for m in range(V):
#         if selected_node[m]:
#             for n in range(V):
#                 if ((not selected_node[n]) and graph[m][n] != sys.maxsize):  
#                     if minimum > graph[m][n]:
#                         minimum = graph[m][n]
#                         a = m
#                         b = n
#     total_weight += graph[a][b]
#     selected_node[b] = True
#     no_edge += 1
# print(total_weight)