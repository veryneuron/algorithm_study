# 풀이 참조 - https://dreamtreeits.tistory.com/m/18
# dfs 여러 case 나올 때 함수로는 list의 주소값이 전달되어 서로 같은 list를 사용할 때 어떻게?
# 그냥 dfs돌리기 전 값 수정하고, 돌린 뒤 복구하면 됨
# 게임 매치를 dfs안에서 생성하는게 아닌 미리 만들어 놔야 함, round수는 한정
# 다른 사람의 풀이 - 모든 경우의 수를 만들고 비교하는 게 아닌, 각 case마다 빼가면서 탐색하는 것

from itertools import combinations

def dfs(round):
    global flag
    if round == 15:
        flag = 1
        if board.count(0) != 18:
            flag = 0
        return
    p1, p2 = game[round]
    for x, y in ((0,2), (1,1), (2,0)):
        if board[p1*3 + x] > 0 and board[p2*3 + y] > 0:
            board[p1*3 + x] -= 1
            board[p2*3 + y] -= 1
            dfs(round+1)
            board[p1*3 + x] += 1
            board[p2*3 + y] += 1

game = list(combinations(range(6), 2))
answer = []
for _ in range(4):
    board = list(map(int, input().split()))
    flag = 0
    dfs(0)
    answer.append(flag)
print(*answer)