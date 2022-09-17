# 시뮬레이션

H, W = map(int, input().split())
init = list(map(int, input().split()))

world = [[False]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if init[j] > 0:
            world[i][j] = True
            init[j] -= 1


result = 0

for x in world:
    buffer = -1
    for idx in range(1,len(x)):
        if buffer == -1:
            if x[idx-1] == True and x[idx] == False:
                buffer = idx
        else:
            if x[idx-1] == False and x[idx] == True:
                if buffer != -1:
                    result += idx - buffer
                    buffer = -1

print(result)

# 다른 사람의 풀이

# 특정 위치 기준으로 왼쪽 제일 큰값과 오른쪽 제일 큰값 구함

result = 0

for w in range(1,W-1):
    result += max(0, min(max(init[:w], default=0), max(init[w+1:], default=0)) - init[w])
print(result)