# 코드 참고 - https://studyandwrite.tistory.com/478

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    s, d = map(int, input().split())
    s -= 1
    d -= 1
    graph[s].append(d)
    graph[d].append(s)

dp = [[0]*2 for _ in range(N)]
visited = [False] * N

def dfs(node):
    visited[node] = True
    dp[node][0], dp[node][1] = 0, 1

    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
            dp[node][0] += dp[neighbor][1]
            dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])

dfs(0)
print(min(dp[0][0], dp[0][1]))