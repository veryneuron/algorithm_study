# N*N 격자판, 1*1 정사각형, 각 칸 좌표 (r,c), 행렬 1부터, 빈칸이거나 벽
# 파이프 2칸, 가로세로 대각선 왼위->오아 가능
# 파이프는 벽 닿으면 x, 오른쪽, 오른쪽아래, 아래로만 길기 가능, 밀면서 45도 회전 가능, 미는방향도 동일
# 가로세로는 2가지 방법, 대각선은 세가지 방법

# BFS 시간초과
import sys
input = sys.stdin.readline

N = int(input())
house = [list(input().split()) for _ in range(N)]
# house = [list(map(int, input().split())) for _ in range(N)]

# def bfs(x, y):
#     q = deque()
#     q.append((x,y,x,y-1))
#     count = 0
#     while q:
#         cur_x, cur_y, prev_x, prev_y = q.popleft()
#         if cur_x == N-1 and cur_y == N-1:
#             count += 1
#             continue
#         if cur_y == prev_y + 1 and cur_x == prev_x:
#             if cur_y + 1 < N and house[cur_x][cur_y + 1] == '0':
#                 q.append((cur_x, cur_y + 1, prev_x, prev_y + 1))
#             if cur_x + 1 < N and cur_y + 1 < N and house[cur_x + 1][cur_y + 1] == '0' and house[cur_x + 1][cur_y] == '0' and house[cur_x][cur_y + 1] == '0':
#                 q.append((cur_x + 1, cur_y + 1, prev_x, prev_y + 1))
#         elif cur_x == prev_x + 1 and cur_y == prev_y:
#             if cur_x + 1 < N and house[cur_x + 1][cur_y] == '0':
#                 q.append((cur_x + 1, cur_y, prev_x + 1, prev_y))
#             if cur_x + 1 < N and cur_y + 1 < N and house[cur_x + 1][cur_y + 1] == '0' and house[cur_x + 1][cur_y] == '0' and house[cur_x][cur_y + 1] == '0':
#                 q.append((cur_x + 1, cur_y + 1, prev_x + 1, prev_y))
#         else:
#             if cur_x + 1 < N and house[cur_x + 1][cur_y] == '0':
#                 q.append((cur_x + 1, cur_y, prev_x + 1, prev_y + 1))
#             if cur_y + 1 < N and house[cur_x][cur_y + 1] == '0':
#                 q.append((cur_x, cur_y + 1, prev_x + 1, prev_y + 1))
#             if cur_x + 1 < N and cur_y + 1 < N and house[cur_x + 1][cur_y + 1] == '0' and house[cur_x + 1][cur_y] == '0' and house[cur_x][cur_y + 1] == '0':
#                 q.append((cur_x + 1, cur_y + 1, prev_x + 1, prev_y + 1))
#     return count


# print(bfs(0,1))

# dfs 시간초과

# count = 0

# def dfs(cur_x, cur_y, prev_x, prev_y):
#     global count
#     if cur_x == N-1 and cur_y == N-1:
#         count += 1
#         return
#     if cur_y == prev_y + 1 and cur_x == prev_x:
#         if cur_y + 1 < N and house[cur_x][cur_y + 1] == '0':
#             dfs(cur_x, cur_y + 1, prev_x, prev_y + 1)
#         if cur_x + 1 < N and cur_y + 1 < N and house[cur_x + 1][cur_y + 1] == '0' and house[cur_x + 1][cur_y] == '0' and house[cur_x][cur_y + 1] == '0':
#             dfs(cur_x + 1, cur_y + 1, prev_x, prev_y + 1)
#     elif cur_x == prev_x + 1 and cur_y == prev_y:
#         if cur_x + 1 < N and house[cur_x + 1][cur_y] == '0':
#             dfs(cur_x + 1, cur_y, prev_x + 1, prev_y)
#         if cur_x + 1 < N and cur_y + 1 < N and house[cur_x + 1][cur_y + 1] == '0' and house[cur_x + 1][cur_y] == '0' and house[cur_x][cur_y + 1] == '0':
#             dfs(cur_x + 1, cur_y + 1, prev_x + 1, prev_y)
#     else:
#         if cur_x + 1 < N and house[cur_x + 1][cur_y] == '0':
#             dfs(cur_x + 1, cur_y, prev_x + 1, prev_y + 1)
#         if cur_y + 1 < N and house[cur_x][cur_y + 1] == '0':
#             dfs(cur_x, cur_y + 1, prev_x + 1, prev_y + 1)
#         if cur_x + 1 < N and cur_y + 1 < N and house[cur_x + 1][cur_y + 1] == '0' and house[cur_x + 1][cur_y] == '0' and house[cur_x][cur_y + 1] == '0':
#             dfs(cur_x + 1, cur_y + 1, prev_x + 1, prev_y + 1)
# dfs(0,1,0,0)
# print(count)

# dp 코드 참고 - https://backtony.github.io/algorithm/2021-03-02-algorithm-boj-class4-44/

dp = [[[0] * N for _ in range(N)] for _ in range(3)]

dp[0][0][1] = 1

for i in range(2, N):
    if house[0][i] == '0':
        dp[0][0][i] = dp[0][0][i - 1]

for r in range(1, N):
    for c in range(1, N):
        if house[r][c] == '0' and house[r][c - 1] == '0' and house[r - 1][c] == '0':
            dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

        if house[r][c] == '0':
            dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
            dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

print(sum(dp[i][N - 1][N - 1] for i in range(3)))