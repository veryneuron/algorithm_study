# 모든 경우의 수 구하면 아마 시간초과
# 각 자리수별로 소팅
# 만약 802랑 9만 남았을때 어떻게?
# 앞자리수만?
# 89이랑 8, 6 남았을때 어떻게?
# 가장 큰 거는 8986, 앞만 보면 구분 x
# 898이랑 89는? 89898 89889
# 898, 89, 8?
# 889, 88, 8?
# 앞에것 같으면 자리수 적은게 우선
# 큰 자리수 중복으로 여러개 나오면 거기서 두번째 자리수 비교
# 그거도 같으면 세번째 자리수 비교
# pseudo
# 각 자리수 정렬
# 가장 큰 자리수 찾음, 개수 하나면 그대로 뺀 뒤 붙이고 다음
# 개수 두개 이상이면 두번째 자리 비교, 3,2자리는 그대로 두번째고 1자리는 자기랑 같은거
# 이유? 두개 이상이니까 3 2자리(숫자가 같음)을 붙이면 되기때문
# 여기서도 중복이면 두번쨰 자리까지 같다는 뜻
# 마찬가지로 3자리는 마지막 자리수, 2자리와 1자리는 자기랑 같은거
# 모든 자리수 개수 0될때까지 반복
# 1:23 포기...

def solution(numbers):
    answer = ''
    digit_three = [x for x in numbers if x >= 100].sort()
    digit_two = [x for x in numbers if 100 > x >= 10].sort()
    digit_one = [x for x in numbers if 10 > x].sort()
    
    while digit_one or digit_two or digit_three:
        first_digit = []
        if len(digit_three) > 0:
            first_digit.append(digit_three[-1]//100)
        else:
            first_digit.append(-1)
        if len(digit_two) > 0:
            first_digit.append(digit_two[-1]//10)
        else:
            first_digit.append(-1)
        if len(digit_one) > 0:
            first_digit.append(digit_one[-1])
        else:
            first_digit.append(-1)
        
        if first_digit.count(max(first_digit)) > 1:
            second_digit = []
            if len(digit_three) > 0:
                second_digit.append(digit_three[-1]//100)
            if len(digit_two) > 0:
                second_digit.append(digit_two[-1]//10)
            if len(digit_one) > 0:
                second_digit.append(digit_one[-1])
            
        
    return answer

# 다른 사람 답
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
# 해석
# 같은 수 사용한다는 idea는 동일함...
# 즉 8같은 숫자는 888로 비교해서 정렬하는것
# 이때 정렬기준만 그렇게 잡고 실제 정렬값은 원래 숫자
# 값은 정렬한숫자 합쳐준뒤 int->str로 바꿔 0000같은 중복 제거