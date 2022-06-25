# 1단계 - 소문자로
# 2단계 - 정규식으로 전부 ''로 치환
# 3단계 - 반복문으로 연속 마침표 제거
# 4단계 - 앞뒤에 마침표 있으면 제거
# 5단계 - 길이 체크해서 0이면 "a" 대입
# 6단계 - 16자 이상이면 15개까지만 살려두고 제거
# 6-1단계 - 마침표가 끝에 있으면 제거
# 7단계 - 길이 2자 이하면 마지막 문자를 길이 3 될때까지 끝에 붙임

# 풀이시간 59분

import re

def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    new_id = "".join(re.findall("[a-z]|\d|-|_|\.", new_id))

    temp = ""
    after_id = ""
    for i in new_id:
        if temp == i == ".":
            continue
        else:
            temp = i
            after_id += i

    # 다른 사람의 풀이 - 정규식 sub(\.+, '.')로 대체가능

    if after_id[:1] == ".":
        after_id = after_id[1:]
    if after_id[-1:] == ".":
        after_id = after_id[:-1]

    # 정규식 sub(^[.]|[.]$, '')로 대체가능
    
    if len(after_id) == 0:
        after_id = "a"

    if len(after_id) >= 16:
        after_id = after_id[:15]
        if after_id[-1:] == ".":
            after_id = after_id[:-1]
    
    if len(after_id) <= 2:
        while len(after_id) < 3:
            after_id += after_id[-1:]

    return after_id