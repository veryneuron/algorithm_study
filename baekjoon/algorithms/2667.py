# 정사각형 지도, 1있는 구역 구분, 그룹 개수 정렬
# bfs 사용
# visited 만들어서 방문여부 표기
# loop 돌면서 1 보이면 그 주변으로 bfs, 수 세면서 visited 표기

N = int(input())
map = [list(input()) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
result = []

def bfs(x, y):
    visited[x][y] = True
    q = []
    q.append((x,y))
    count = 0
    while q:
        cur_x, cur_y = q.pop()
        count += 1
        if cur_x - 1 >= 0 and not visited[cur_x - 1][cur_y] and map[cur_x - 1][cur_y] == '1':
            visited[cur_x - 1][cur_y] = True
            q.append((cur_x - 1, cur_y))
        if cur_y - 1 >= 0 and not visited[cur_x][cur_y - 1] and map[cur_x][cur_y - 1] == '1':
            visited[cur_x][cur_y - 1] = True
            q.append((cur_x, cur_y - 1))
        if cur_x + 1 < N and not visited[cur_x + 1][cur_y] and map[cur_x + 1][cur_y] == '1':
            visited[cur_x + 1][cur_y] = True
            q.append((cur_x + 1, cur_y))
        if cur_y + 1 < N and not visited[cur_x][cur_y + 1] and map[cur_x][cur_y + 1] == '1':
            visited[cur_x][cur_y + 1] = True
            q.append((cur_x, cur_y + 1))
    return count

for x in range(N):
    for y in range(N):
        if map[x][y] == '1' and not visited[x][y]:
            result.append(bfs(x, y))
print(len(result))
print(*sorted(result), sep='\n')

