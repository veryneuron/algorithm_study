# 양의 정수 n, k진수로 변환, 그랬을 때 소수의 개수
# 0P0, P0, 0P, P, P 안에는 0이 없어야 함 P는 10진법 소수
# 진법 변환 > 소수 구하기
# 진법 변환? k^12345... 로 계속 나누면서 0 될때까지, 매번 결과 list에 넣음
# 소수 구하기? 스택 사용, 0나오면 있는거 전부 꺼냄, 결과 list에 넣고 0있거나 소수 아닌거 빼냄
# 59:20
# 다른 사람의 풀이 - 나눌때 split('0') 하면 알아서 나눠짐...

from collections import deque

def check_prime(num):
    if num == 1: return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = []
    k_base = []

    while n > 0:
        digit = n % k
        k_base.append(digit)
        n //= k
    k_base.reverse()

    num_list = []
    dq = deque()
    for idx, number in enumerate(k_base):
        if number != 0:
            dq.append(number)
        if number == 0 or idx == len(k_base) - 1:
            if dq:
                temp_str = ""
                while dq:
                    temp_str += str(dq.popleft())
                if check_prime(int(temp_str)):
                    answer.append(int(temp_str))   
                    
    return len(answer)

# 다른 사람의 풀이 참고 - split('0') 사용

def check_prime(num):
    if num == 1: return False
    for i in range(2, int(num**(1/2)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    answer = []
    k_base = ""

    while n > 0:
        digit = n % k
        k_base = str(digit) + k_base
        n //= k

    count = 0

    for num in k_base.split('0'):
        if not num: continue
        if check_prime(int(num)):
            count += 1
                    
    return count