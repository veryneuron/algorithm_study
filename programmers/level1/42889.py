# idea - 실패율 구하고 튜플로 reverse sort
#
# psuedo
# iterate N
# 실패율 구함
# 분자는 count n, 분모는 n 이상인거 filter
# 튜플로 answer에 append함
# sort answer, key는 실패율
# 풀이시간 46분

def solution(N, stages):
    answer = []

    for n in range(1,N+1):
        reached = len(list(filter(lambda x: x>=n, stages)))
        if reached == 0:
            answer.append((n,0))
        else:
            answer.append((n, stages.count(n) / reached))
        
    return list(map(lambda x: x[0], sorted(answer, key=lambda x: x[1], reverse=True)))