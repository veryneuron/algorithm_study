def solution(phone_book):
    answer = True
    result_set = set()
    for num in phone_book:
        result_set.add(num)
    for num in phone_book:
        for i in range(1,len(num)):
            if num[0:i] in result_set:
                return False
    return answer

    # 왜 해시...? key값 존재유무만 확인하는데 굳이?