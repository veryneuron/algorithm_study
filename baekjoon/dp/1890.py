N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
# dp[0][0] = 1

# for i in range(N):
#     for j in range(N):
#         if map[i][j] != 0:
#             len = map[i][j]
#             if i + len < N:
#                 dp[i+len][j] += dp[i][j]
#             if j + len < N:
#                 dp[i][j+len] += dp[i][j]

# print(dp[N-1][N-1])

# 다른 사람의 풀이 - recursion 사용, 반대로 끝에서부터 시작으로(왜냐면 특정 칸에서 이전 정보를 몰라서)

def aux(row, col):
    if row == N-1 and col == N-1:
        return 1
    if dp[row][col] != 0:
        return dp[row][col]
    current = 0
    if map[row][col] != 0:
        len = map[row][col]
        if row + len < N:
            current += aux(row+len, col)
        if col + len < N:
            current += aux(row, col+len)
    dp[row][col] = current
    return current

print(aux(0,0))