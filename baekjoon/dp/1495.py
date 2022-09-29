N, S, M = map(int, input().split())
V = list(map(int, input().split()))
before = {S}

for i in range(N):
    after = set()
    for b in before:
        if b+V[i] <= M:
            after.add(b+V[i])
        if 0 <= b-V[i]:
            after.add(b-V[i])
    before = after

if len(after) > 0:
    print(max(after))
else:
    print(-1)