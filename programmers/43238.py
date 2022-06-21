def solution(n, times):
    min_val = 1
    max_val = max(times) * n

    while min_val < max_val:
        mid_val = (min_val + max_val) // 2
        if n <= sum([mid_val // time for time in times]):
            max_val = mid_val
        else:
            min_val = mid_val + 1
    return min_val

print(solution(6,[7,10]))