# 최소연료 구하기 / bfs, 시뮬레이션
# x! dp

import sys

def in_range(y, x):
    global N
    return 0 <= y < N and 0 <= x < N

def dfs(y, x, fuel):
    global g_fuel, N, g_tunnel, g_field, g_visited
    if fuel > g_fuel:
        return
    if y == N-1 and x == N-1:
        g_fuel = min(g_fuel, fuel)
        return
    if (y, x) in g_tunnel:
        for ty, tx, c in g_tunnel[(y, x)]:
            next_fuel = fuel+c
            if not g_visited[ty][tx] and next_fuel < g_dp[ty][tx]:
                g_visited[ty][tx] = True
                dfs(ty, tx, fuel+c)
                g_visited[ty][tx] = False
    for dy, dx in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
        if in_range(y+dy, x+dx) and not g_visited[y+dy][x+dx]:
            g_visited[y+dy][x+dx] = True
            next = g_field[y+dy][x+dx]
            now = g_field[y][x]
            if next > now:
                next_fuel = fuel + ((next - now) * 2)
                if next_fuel < g_dp[y+dy][x+dx]:
                    dfs(y+dy, x+dx, next_fuel)
                    g_visited[y+dy][x+dx] = False
            elif next < now:
                if fuel < g_dp[y+dy][x+dx]:
                    dfs(y+dy, x+dx, fuel)
                    g_visited[y+dy][x+dx] = False
            else:
                if fuel+1 < g_dp[y+dy][x+dx]:
                    dfs(y+dy, x+dx, fuel+1)
                    g_visited[y+dy][x+dx] = False


TC = int(input())

answer = []
g_fuel = sys.maxsize
g_visited = []
g_field = []
g_tunnel = {}
g_dp = []
N = 0

for _ in range(TC):
    N, M = map(int, input().split())
    g_field = [[] for _ in range(N)]
    g_dp = [[sys.maxsize]*N for _ in range(N)]
    for i in range(N):
        g_field[i].extend(list(map(int, input().split())))
    g_tunnel = {}
    for _ in range(M):
        Ay, Ax, By, Bx, C = map(int, input().split())
        Ay, Ax, By, Bx = Ay-1, Ax-1, By-1, Bx-1
        if (Ay, Ax) in g_tunnel:
            g_tunnel[(Ay, Ax)].append((By, Bx, C))
        else:
            g_tunnel[(Ay, Ax)] = [(By, Bx, C)]
        if (By, Bx) in g_tunnel:
            g_tunnel[(By, Bx)].append((Ay, Ax, C))
        else:
            g_tunnel[(By, Bx)] = [(Ay, Ax, C)]
        
    g_visited = [[False]*N for _ in range(N)]
    g_visited[0][0] = True
    g_dp[0][0] = 0
    g_fuel = sys.maxsize
    dfs(0, 0, 0)

    answer.append(g_fuel)


for tc in range(TC):
    print(f'#{tc+1} {answer[tc]}')