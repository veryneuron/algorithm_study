# n*n 보드에 연속으로 있는 행 or 열 사탕, 교환 한번 가능
# 14:05 포기!! 아이디어가 도저히 생각나지 않음...
# 아이디어 참고 - 완전탐색
# pseudo
# 시작전에 매 index 체크해서 가장 큰 거 세이브
# 매 index마다 가로세로 전부 확인해서 바꿨을 떄 최대길이 확인 
# 1:34 구현 포기...
# 다른 사람의 풀이 참고, 계산하는 함수는 놔두고 가로세로 싹다 바꿔보고 바꾸기 전이랑 비교
# if 비교문 안쓰고 max 내장함수 사용하면 시간 초과남 ㅡㅡ;

import sys
input = sys.stdin.readline

def find_max_length(board):
    local_len = 1
    for x in range(N):
        count = 1
        for y in range(1, N):
            if board[x][y] == board[x][y-1]:
                count += 1
            else:
                count = 1
            if count > local_len:
                local_len = count
        count = 1
        for y in range(1, N):
            if board[y][x] == board[y-1][x]:
                count += 1
            else:
                count = 1
            if count > local_len:
                local_len = count
    return local_len

N = int(input())
input = [list(input()) for _ in range(N)]
maximum = 0

for x in range(N):
    for y in range(N):
        if y+1 < N:
            input[x][y], input[x][y+1] = input[x][y+1], input[x][y]
            temp = find_max_length(input)
            if temp > maximum:
                maximum = temp

            input[x][y], input[x][y+1] = input[x][y+1], input[x][y]
        if x+1 < N:
            input[x][y], input[x+1][y] = input[x+1][y], input[x][y]
            temp = find_max_length(input)
            if temp > maximum:
                maximum = temp
            input[x][y], input[x+1][y] = input[x+1][y], input[x][y]
print(maximum)