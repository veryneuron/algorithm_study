# idea - number P 1~len(number) 로 값 다 구해놓고 각각 소수 test, 총 결과 sum

# psuedo
# 1~nubers 크기까지 Permutation 생성
# 각 Permutation 만들어 질때마다 순회
# string join하고 숫자로 바꿈
# prime num인지 test 후, prime num이면 answer++
# prime num? 2부터 순회하면서 나눠서 나머지 0인거 있으면 소수 아닌것
# 풀이시간 1:14

from itertools import permutations
import math

def solution(numbers):
    answer = 0
    result = set()
    for i in range(1,len(numbers)+1):
        for p in set(permutations(numbers, i)):
            result.add(int(''.join(p)))
            
    for i in result:
        if is_prime(i):
            answer += 1
    return answer

def is_prime(num):
    flag = True
    if num <= 1:
        return False
    elif num > 1:
        for i in range(2,int(math.floor(math.sqrt(num)+1))):
            if (num % i) == 0:
                flag = False
                break
    return flag