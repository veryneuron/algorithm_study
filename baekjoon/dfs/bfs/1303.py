N, M = map(int, input().split())

from collections import deque

war = [list(input()) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

def bfs(row, column):
    visited[row][column] = True
    team = war[row][column]
    power = 0
    dq = deque()
    dq.append((row, column))
    while dq:
        now_row, now_column = dq.popleft()
        power += 1
        if now_row + 1 < M and war[now_row + 1][now_column] == team and visited[now_row + 1][now_column] == False:
            dq.append((now_row + 1, now_column))
            visited[now_row + 1][now_column] = True
        if now_column + 1 < N and war[now_row][now_column + 1] == team and visited[now_row][now_column + 1] == False:
            dq.append((now_row, now_column + 1))
            visited[now_row][now_column + 1] = True
        if now_row - 1 >= 0 and war[now_row - 1][now_column] == team and visited[now_row - 1][now_column] == False:
            dq.append((now_row - 1, now_column))
            visited[now_row - 1][now_column] = True
        if now_column - 1 >= 0 and war[now_row][now_column - 1] == team and visited[now_row][now_column - 1] == False:
            dq.append((now_row, now_column - 1))
            visited[now_row][now_column - 1] = True
    return power**2

white = 0
blue = 0

for r in range(M):
    for c in range(N):
        if visited[r][c] == False:
            if war[r][c] == 'W':
                white += bfs(r, c)
            else:
                blue += bfs(r,c)
print(white, blue)