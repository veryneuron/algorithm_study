import sys
sys.setrecursionlimit(10**6) # 없으면 에러... 백준의 상태가???
N = int(input())
population = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, d = map(int, input().split())
    tree[s].append(d)
    tree[d].append(s)

dp = [[0, population[i]] for i in range(N+1)]
visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    
    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][1] += dp[child][0]
            dp[node][0] += max(dp[child][0], dp[child][1])
            # 다른 사람의 풀이를 참고했으나, 이러면 조건 3(우수 x인 마을은 적어도 하나의 우수 마을과 인접)을 만족하지 못하지 않나?
            # 만약 max값으로 더 큰 값을 골랐을 때, 계속해서 비우수 마을만 나와서 모든 인접 노드가 비우수 마을이 된다면?
            # 이 경우 하나의 우수 마을을 추가해 줘야 되는게 아닌가?
            # 어째서인지 제출했을때 성공함...
    # 우수 마을 추가해주는 코드, 어째선지 값이 다름...
    # max_val = 0
    # flag = False
    # for child in tree[node]:
    #     if not visited[child]:
    #         if dp[child][0] > dp[child][1]:
    #             max_val += dp[child][0]
    #         else:
    #             max_val += dp[child][1]
    #             flag = True
    # idx = node
    # temp = -sys.maxsize
    # if not flag:
    #     for child in tree[node]:
    #         if not visited[child]:
    #             if temp < (dp[child][1] - dp[child][0]):
    #                 temp = dp[child][1] - dp[child][0]
    #                 idx = child
    # dp[node][0] = max_val + dp[idx][1] - dp[idx][0]
    # print(dp)

dfs(1)
print(max(dp[1][0], dp[1][1]))