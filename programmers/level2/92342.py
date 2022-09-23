# 라이언 vs 어피치
# 라이언 불리, 순서는 어피치 n발 후 라이언 n발
# 안쪽 10, 밖은 0
# 각 점수 기준 계산, 어피치 라이언 중 더 많은 화살 맞춘 쪽이 적혀있는 점수 획득, 같으면 어피치 점수 획득
# 어피치 n발 쏘기 완료, 라이언 차례, 가장 큰 점수 차이로 이기기 위한 과녁 점수
# return값은 10점부터 0점까지 화살개수, 우승 못하면 -1 return
# 같은 점수차 여러 개 일때 가장 낮은 점수를 더 맞힌 경우 return
# 라이언이 점수 따려면 무조건 화살갯수 +1 되야함
# dfs 완전탐색?
# 풀이시간 2:02, 구현이 힘들다...

high_score_list = []
high_score = 0
cost = []

def get_score(score):
    result = 0
    apeach_score = [x-1 for x in cost]
    apeach, ryan = 0, 0
    for idx, (a, r) in enumerate(zip(reversed(apeach_score), reversed(score))):
        if r or a:
            if r > a:
                ryan += idx
            else:
                apeach += idx
    return ryan - apeach
def min_list(list1, list2):
    for l1, l2 in zip(reversed(list1), reversed(list2)):
        if l1 > l2:
            return list1
        elif l2 > l1:
            return list2
    return list1

def dfs(idx, score, arrow):
    global cost, high_score, high_score_list
    if idx == 9:
        score.append(arrow)
    elif arrow == 0:
        while len(score) < 11:
            score.append(0)
    if idx == 9 or arrow == 0:
        cur_score = get_score(score)
        if cur_score > high_score:
            high_score = cur_score
            high_score_list = score
        elif cur_score == high_score:
            min = min_list(score, high_score_list)
            high_score = get_score(min)
            high_score_list = min
    else:
        if arrow - cost[idx+1] >= 0:
            dfs(idx+1, [*score, cost[idx+1]], arrow - cost[idx+1])
        dfs(idx+1, [*score, 0], arrow)
        
def solution(n, info):
    global cost
    cost = [x+1 for x in info]
    dfs(-1, [], n)
    if high_score > 0:
        return high_score_list
    else:
        return [-1]