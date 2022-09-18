# 완전탐색
# a, n, t, i, c는 무조건 포함
# pseudo
# 단어 집합 생성
# 각 집합에서 글자만 추출
# 글자에서 combination
# combination 루프돌면서 subset 개수 확인
# 최대값 출력

from itertools import combinations

N, K = map(int, input().split())

words = [set(input()) for _ in range(N)]

alphabet = set.union(*words).difference({'a', 'c', 'i', 'n', 't'})

max_val = 0

if K > 5:
    if len(alphabet) == 0:
        comb = {'a'}
    elif K-5 > len(alphabet):
        comb = combinations(alphabet, len(alphabet))
    else:
        comb = combinations(alphabet, K-5)
    for c in comb:
        count = 0
        c = set(c)
        c.update({'a', 'c', 'i', 'n', 't'})
        for w in words:
            if w.issubset(c):
                count += 1
        max_val = max(max_val, count)
elif K == 5:
    for w in words:
        if w.issubset({'a', 'c', 'i', 'n', 't'}):
            max_val += 1

print(max_val)