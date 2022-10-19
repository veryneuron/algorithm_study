def in_range(row, column):
    return 0 <= row < 12 and 0 <= column < 6

def dfs(r, c):
    for dr, dc in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
        if in_range(r+dr, c+dc) and field[r+dr][c+dc] == origin and not visited[r+dr][c+dc]:
            visited[r+dr][c+dc]  = True
            chain.append((r+dr, c+dc))
            dfs(r+dr, c+dc)

field = [[] for _ in range(12)]
for i in range(12):
    field[i].extend(list(input()))



answer = 0
while True:
    boom = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                chain = [(i, j)]
                origin = field[i][j]
                dfs(i, j)
                if len(chain) > 3:
                    boom  = True
                    for r, c in chain:
                        field[r][c] = '.'
    if boom:
        answer += 1
    else:
        break

    for j in range(6):
        temp = []
        for i in range(12):
            if field[i][j] != '.':
                temp.append(field[i][j])
                field[i][j] = '.'
        for idx, t in enumerate(reversed(temp)):
            field[11-idx][j] = t

print(answer)