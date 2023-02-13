# 최소연료 구하기 / bfs, 시뮬레이션
# x! dp + bfs로 전환!

from collections import deque

def in_range(y, x):
    global N
    return 0 <= y < N and 0 <= x < N

TC = int(input())

answer = []
g_fuel = 1e9
g_field = []
g_tunnel = {}
g_dp = []
N = 0

for _ in range(TC):
    N, M = map(int, input().split())
    g_field = [[] for _ in range(N)]
    g_dp = [[1e9]*N for _ in range(N)]
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
    g_dp[0][0] = 0
    g_fuel = 1e9
    dq = deque()
    dq.append((0, 0, 0))
    while dq:
        y, x, fuel = dq.popleft()
        if y == N-1 and x == N-1:
            g_fuel = min(g_fuel, fuel)
            continue
        if fuel >= g_fuel:
            continue
        if (y, x) in g_tunnel:
            for ty, tx, c in g_tunnel[(y, x)]:
                next_fuel = fuel+c
                if next_fuel < g_dp[ty][tx]:
                    g_dp[ty][tx] = next_fuel
                    dq.append((ty, tx, next_fuel))
        for dy, dx in {(1, 0), (0, 1), (-1, 0), (0, -1)}:
            if in_range(y+dy, x+dx):
                next = g_field[y+dy][x+dx]
                now = g_field[y][x]
                if next > now:
                    next_fuel = fuel + ((next - now) * 2)
                elif next < now:
                    next_fuel = fuel
                else:
                    next_fuel = fuel+1
                if next_fuel < g_dp[y+dy][x+dx]:
                    g_dp[y+dy][x+dx] = next_fuel
                    dq.append((y+dy, x+dx, next_fuel))
    answer.append(g_fuel)


for tc in range(TC):
    print(f'#{tc+1} {answer[tc]}')