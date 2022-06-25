# idea - 일치한 갯수가 최저순위, 거기에 0개수 더한게 최고순위

# pseudo
# lottos 순회하면서 win_nums와 일치여부 확인
# lottos의 0 개수 구함
# 일치한 개수 + 0개수로 최고순위, 일치한 개수로 최저순위 구한 뒤 return
# 풀이시간 20분

def solution(lottos, win_nums):
    answer = []

    correct = 0
    zero_count = 0

    for l in lottos:
        if l in win_nums:
            correct += 1
        elif l == 0:
            zero_count += 1
    tabular = [x for x in range(7, 0, -1)]
    tabular[0] = 6

    answer.extend([tabular[correct+zero_count], tabular[correct]])
    return answer