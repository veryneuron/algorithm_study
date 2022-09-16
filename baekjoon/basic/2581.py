# 에라토스테네스의 체

M = int(input())
N = int(input())

num_list = []
multiples = []
for i in range(2, N+1):
    if i not in multiples:
        if i >= M:
            num_list.append(i)
        for j in range(i*i, N+1, i): # i보다 작은건 이미 추가되어 있음!
            multiples.append(j)
if num_list:
    print(sum(num_list), num_list[0], sep='\n')
else:
    print(-1)
