# 떨어지지 않은 기간
# 특정 시점에서 그 이전 가격들중 떨어지지 않은 건 +, 떨어진 건 확정
# 아니면 하나하나 전부 계산...?
# for문 두번, price하나씩이랑 각 기간 계산
# 효율성의 상태가???
# 27
def solution(prices):
    answer = []
    
    for idx, p in enumerate(prices):
        time = 0
        for i in range(idx, len(prices)-1):
            time += 1
            if prices[idx] <= prices[i+1]:
                continue
            else:
                break
        answer.append(time)
        
    return answer