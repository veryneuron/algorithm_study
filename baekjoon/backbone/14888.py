# 재귀 탐색

input()
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def recursion(num_list, opr_list):
    result = set()

    if len(num_list) == 1:
        result.add(num_list[0])
        return result
    
    if opr_list[0] > 0:
        for i in recursion(num_list[:len(num_list)-1], [opr_list[0]-1, opr_list[1], opr_list[2], opr_list[3]]):
            result.add(i + num_list[-1])
    if opr_list[1] > 0:
        for i in recursion(num_list[:len(num_list)-1], [opr_list[0], opr_list[1]-1, opr_list[2], opr_list[3]]):
            result.add(i - num_list[-1])
    if opr_list[2] > 0:
        for i in recursion(num_list[:len(num_list)-1], [opr_list[0], opr_list[1], opr_list[2]-1, opr_list[3]]):
            result.add(i * num_list[-1])
    if opr_list[3] > 0:
        for i in recursion(num_list[:len(num_list)-1], [opr_list[0], opr_list[1], opr_list[2], opr_list[3]-1]):
            if (0 > i):
                result.add(-(-i // num_list[-1]))
            else:
                result.add(i // num_list[-1])

    return result

result_set = recursion(numbers, operators)
print(max(result_set), min(result_set), sep='\n')

# return값 없이 바로구하기(다른 사람의 풀이)

import sys

min_val = sys.maxsize
max_val = -sys.maxsize

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def recursion(idx, opr_list, result):
    global max_val, min_val
    
    if idx == N:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
    
    if opr_list[0] > 0:
        recursion(idx+1, [opr_list[0]-1, opr_list[1], opr_list[2], opr_list[3]], result + numbers[idx])
    if opr_list[1] > 0:
        recursion(idx+1, [opr_list[0], opr_list[1]-1, opr_list[2], opr_list[3]], result - numbers[idx])
    if opr_list[2] > 0:
        recursion(idx+1, [opr_list[0], opr_list[1], opr_list[2]-1, opr_list[3]], result * numbers[idx])
    if opr_list[3] > 0:
        recursion(idx+1, [opr_list[0], opr_list[1], opr_list[2], opr_list[3]-1], int(result / numbers[idx]))

recursion(1, operators, numbers[0])

print(max_val)
print(min_val)