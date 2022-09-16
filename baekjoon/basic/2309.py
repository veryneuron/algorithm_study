from itertools import combinations

heights = [int(input()) for _ in range(9)]

def comb_n(lst, n):
    if n == 0:
        return [[]]

    result = []

    for i in range(len(lst)):
        m = lst[i]
        rem_lst = lst[i+1:]

        remainlst_com = comb_n(rem_lst, n-1)
        for p in remainlst_com:
            result.append([m, *p])

    return result

for height in comb_n(heights, 7):
    if sum(height) == 100:
        print(*sorted(height), sep='\n')
        break

# with itertools

for height in list(combinations(heights, 7)):
    if sum(height) == 100:
        print(*sorted(height), sep='\n')
        break
