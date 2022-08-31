# N개중 N/2마리 - 중복가능
# 최대한 많은 가짓수
# input 종류 list인 nums - 200000이하 자연수, 길이 10000이하& 짝수(N/2 는 무조건 자연수)
# output 종류 개수"만"(가짓수 x)
# idea: 해시...? 그냥 입력받은 nums set에 넣어 중복 제거후 가짓수 return
# 만약 N/2가 set크기보다 많다면? 어처피 개수만 return하면되기 때문에 상관 x
# pseudo
# nums 원소 set에 넣기
# set 크기가 N/2보다 크면 N/2 return, 아니면 set크기 return
# 풀이시간 14:29
# 다른 사람의 풀이 - min 함수가 있었음!!!


def solution(nums):
    nums_set = set(nums)
    return len(nums)/2 if len(nums_set) > len(nums)/2 else len(nums_set)