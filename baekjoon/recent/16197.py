from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
coin = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin.append((i, j))

visited = []

dq = deque()
dq.append((coin, 0))
visited.append(coin)
result = -1

while dq:
    current, button = dq.popleft()
    if button == 10:
        break
    for dr, dc in (1,0),(0,1),(-1,0),(0,-1):
        first_new_row = current[0][0] + dr
        first_new_col = current[0][1] + dc
        second_new_row = current[1][0] + dr
        second_new_col = current[1][1] + dc
        if 0 <= first_new_row < N and 0 <= first_new_col < M and board[first_new_row][first_new_col] == '#':
            first_new_row = current[0][0]
            first_new_col = current[0][1]
        if 0 <= second_new_row < N and 0 <= second_new_col < M and board[second_new_row][second_new_col] == '#':
            second_new_row = current[1][0]
            second_new_col = current[1][1]
        if ((first_new_row >= N or first_new_row < 0) or (first_new_col >= M or first_new_col < 0)
             and 0 <= second_new_row < N and 0 <= second_new_col < M):
            result = button+1
            break
        if ((second_new_row >= N or second_new_row < 0) or (second_new_col >= M or second_new_col < 0)
             and 0 <= first_new_row < N and 0 <= first_new_col < M):
             result = button+1
             break
        if (0 <= first_new_row < N and 0 <= second_new_row < N and 0 <= first_new_col < M and 0 <= second_new_col < M
            and [(first_new_row, first_new_col), (second_new_row, second_new_col)] not in visited):
            visited.append([(first_new_row, first_new_col), (second_new_row, second_new_col)])
            dq.append(([(first_new_row, first_new_col), (second_new_row, second_new_col)], button+1))
    else:
        continue
    break
print(result)