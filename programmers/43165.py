def solution(numbers, target):
    return DFS(numbers, target, 0, 0)

def DFS(numbers, target, current, depth):
    if depth == len(numbers):
        if current == target:
            return 1
        else:
            return 0
    else:
        a = DFS(numbers, target, current+numbers[depth], depth+1)
        b = DFS(numbers, target, current-numbers[depth], depth+1)
        return a + b