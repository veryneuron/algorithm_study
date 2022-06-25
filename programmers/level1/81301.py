# idea - ??? 간단한건 replace노가다, 아니면 list의 index가지고도 할 수있을것 같긴 하지만...
# 풀이시간 7분

def solution(s):
    answer = 0
    s = s.replace("zero","0")
    s = s.replace("one","1")
    s = s.replace("two","2")
    s = s.replace("three","3")
    s = s.replace("four","4")
    s = s.replace("five","5")
    s = s.replace("six","6")
    s = s.replace("seven","7")
    s = s.replace("eight","8")
    s = s.replace("nine","9")

    return int(s)