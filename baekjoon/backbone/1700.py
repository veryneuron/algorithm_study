# 그리디

# 해답 참조
# 뽑을때 가장 나중에 쓰이는거 뽑음

# pseudo
# 플러그 비어있으면 그냥 꽃음
# 플러그 꽉차면 그리디 알고리즘 작동
# 뒤쪽 리스트 하나씩 확인하면서 
N, K = map(int, input().split())

plug = list(map(int, input().split()))
multi = []
unplug = 0

for idx, p in enumerate(plug):
    if p in multi:
        continue
    elif len(multi) < N:
        multi.append(p)
    else:
        multi_idx = [101] * N
        for i in range(len(multi)):
            if multi[i] in plug[idx:]:
                multi_idx[i] = plug[idx:].index(multi[i])

        multi[multi_idx.index(max(multi_idx))] = p
        unplug += 1

print(unplug)

