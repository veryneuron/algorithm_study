# 다익스트라

# 다른 사람의 풀이 참고

import heapq
import sys

# 이거 없으면 시간 초과남;;
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, weight = map(int, input().split())
    graph[s].append((weight, e))
start, end = map(int, input().split())

costs = [sys.maxsize] * (N+1)
costs[start] = 0
visited = set()

pq = []
heapq.heappush(pq, (0, start))
while pq:
    cost, current_vertex = heapq.heappop(pq)
    if current_vertex in visited:
        continue
    else:
        visited.add(current_vertex)

    for cur_wei, cur_end in graph[current_vertex]:
        new_cost = cost + cur_wei
        if costs[cur_end] > new_cost:
            costs[cur_end] = new_cost
            heapq.heappush(pq, (new_cost, cur_end))

print(costs[end])

# 인접행렬

input = sys.stdin.readline

N = int(input())
graph = [[sys.maxsize]*(N+1) for _ in range(N+1)]
for _ in range(int(input())):
    s, e, weight = map(int, input().split())
    graph[s][e] = min(weight, graph[s][e])
start, end = map(int, input().split())

costs = [sys.maxsize] * (N+1)
costs[start] = 0
visited = set()

pq = []
heapq.heappush(pq, (0, start))
while pq:
    cost, current_vertex = heapq.heappop(pq)
    if current_vertex in visited:
        continue
    else:
        visited.add(current_vertex)

    for idx, weight in enumerate(graph[current_vertex]):
        if weight == sys.maxsize: continue
        new_cost = cost + weight
        if costs[idx] > new_cost:
            costs[idx] = new_cost
            heapq.heappush(pq, (new_cost, idx))

print(costs[end])