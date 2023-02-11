N, M = map(int, input().split())

populations = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())

town_number = [list(map(int, input().split())) for _ in range(Q)]

populations.sort(key = lambda x: x[0])

result = []

for number in town_number:
    count = 0
    for pop in populations:
        if pop[0] > number[1]:
            break
        elif number[0] <= pop[0]:
            count += pop[1]
    result.append(count)

print(*result, sep='\n')