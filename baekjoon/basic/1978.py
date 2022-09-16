# 단순한 방법

def is_prime(number):
    if number == 1 :
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
input()
numbers = list(map(int, input().split()))
print(sum(map(is_prime, numbers)))

# 수학적 최적화

from math import sqrt

def is_prime(number):
    if number == 1 :
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True