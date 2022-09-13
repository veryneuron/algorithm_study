N = input()
values = map(int, input().split())

max = -1000000
min = 1000000

for value in values:
    if value > max:
        max = value
    if value < min:
        min = value

print(min, max, end=' ')


