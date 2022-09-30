N = int(input())

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True

# result = []
# def recursion(idx, buffer):
#     if idx == N:
#         result.extend(buffer)
#         return
#     for i in range(1,10):
#         recursion(idx+1, [i+b*10 for b in buffer if isPrime(i+b*10)])
# recursion(1, [2,3,5,7])
# print(*sorted(result), sep='\n')

# 다른 사람의 풀이 - list가 아닌 수 자체를 dfs하면 속도가 훨씬 빨라짐

result = []
def dfs(idx, num):
    if not isPrime(num):
        return
    if idx == N:
        result.append(num)
        return
    for i in range(1,10, 2):
        dfs(idx+1, num*10+i)
for i in [2,3,5,7]:
    dfs(1, i)
print(*sorted(result), sep='\n')