# idea - 각 array 2진수로 변환 후 bit masking, 벽은 |로, 공백은 &로 >> 벽이 1이면 그냥 전체 or연산하면 됨!
#
# pseudo
# arr1, arr2 각 원소 이진수 변환
# 그 뒤로 하나씩 가져와서 iterate
# | bitwise 연산
# 0이면 공백, 1이면 #을 answer의 string에 붙임

# 막힌 부분 - index 순회 어디서 할지 꼼꼼히 체크할 것 ㅠㅠ 에러난 코드에서 for b~안에서 idx 설정했음
# + bin 사용시 주의점 - 앞자리 0이면 그냥 없애버림!
# 풀이시간 1:02

def solution(n, arr1, arr2):
    answer = [""] * n

    for idx, (x, y) in enumerate(zip(arr1, arr2)):
        for b in bin(x|y)[2:].zfill(n):
            if b == "0":
                answer[idx] += " "
            else:
                answer[idx] += "#"

    return answer
# 풀이 후 - 굳이 binary string 하나하나 확인해야 될까?

def solution_2(n, arr1, arr2):
    answer = [""] * n

    for idx, (x, y) in enumerate(zip(arr1, arr2)):
            answer[idx] += bin(x|y)[2:].zfill(n).replace("0"," ").replace("1","#")

    return answer

# 굳이 idx 사용할 필요가..?

def solution_3(n, arr1, arr2):
    return [bin(x|y)[2:].zfill(n).replace("0"," ").replace("1","#") for x, y in zip(arr1,arr2)]