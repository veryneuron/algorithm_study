from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

result = []

def bfs(row, column):
    global count
    visited[row][column] = True
    dq = deque()
    dq.append((row, column, 1))
    while dq:
        row, column, count = dq.popleft()
        if row == N-1 and column == M-1:
            result.append(count)
        for dr, dc in (1,0),(0,1),(-1,0),(0,-1):
            new_row = row + dr
            new_column = column + dc
            if not(0 <= new_row < N) or not(0 <= new_column < M):
                continue
            if visited[new_row][new_column] == False and maze[new_row][new_column] == '1':
                visited[new_row][new_column] = True
                dq.append((new_row, new_column, count+1))

bfs(0, 0)

print(min(result))