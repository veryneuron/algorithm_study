# 홀수날 키1성장, 짝수날 키2성장, 안뿌릴수도있음
# 완전탐색... - x! 그리디?

import sys

min_days = sys.maxsize

def dfs(water_list, days, is_odd):
    global min_days
    # print(f"water list - {water_list}, days - {days}")
    if days > min_days:
        return
    if sum(water_list) == 0:
        min_days = min(days, min_days)
    for i in range(len(water_list)):
        if is_odd:
            if water_list[i] > 0:
                if water_list[i] >= 2:
                    dfs(water_list, days+1, not is_odd)
                water_list[i] -= 1
                dfs(water_list, days+1, not is_odd)
                water_list[i] += 1
        else:
            if water_list[i] >= 2:
                water_list[i] -= 2
                dfs(water_list, days+1, not is_odd)
                water_list[i] += 2
            elif water_list[i] > 0:
                dfs(water_list, days+1, not is_odd)

TC = int(input())
answer = []
for _ in range(TC):
    N = int(input())
    heights = list(map(int, input().split()))
    min_days = sys.maxsize
    water_list = list(map(lambda x: max(heights) - x, heights))
    dfs(water_list, 0, True)
    answer.append(min_days)
for tc in range(TC):    
    print(f'#{tc+1} {answer[tc]}')