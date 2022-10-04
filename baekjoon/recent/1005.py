from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    graph = [[] for _ in range(N)]
    inorder = [0] * N
    for _ in range(K):
        s, d = map(int, input().split())
        s -= 1
        d -= 1
        graph[s].append(d)
        inorder[d] += 1
    end = int(input())
    end -= 1

    time = 0
    dp = [0] * N
    dq = deque()
    for i in range(N):
        if inorder[i] == 0:
            dq.append(i)
            dp[i] += D[i]
    prev_depth = -1
    
    while dq:
        node = dq.popleft()

        for g in graph[node]:
            inorder[g] -= 1
            dp[g] = max(dp[g], dp[node] + D[g])
            if inorder[g] == 0:
                dq.append(g)

    print(dp[end])

# max 구할때 dp사용