max_value, current = 0, 0
for _ in range(10):
    off, on = map(int, input().split())
    current += on - off
    max_value = max(max_value, current)
print(max_value)