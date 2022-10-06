# 파싱 후 맨 앞꺼는 공통부분, 그리고 각 청크마다 글자만 분리 후 나머지는 뒤집어서 공통쪽에
# 정규식 사용?
# 55:09 맞았다... 하지만 정규식 안쓰는게 더 나아보임

import re

input = list(input().split())
common = input[0]
for word in input[1:]:
    name = re.findall('[a-zA-Z]+', word)
    type = re.findall('\*|\[\]|\&', word[:-1])
    type.reverse()
    print(common+''.join(type)+' '+str(*name)+';')

# 다른 사람의 풀이 - 정규식 안쓴버전, 왼쪽부터 if문으로 하나씩 조건분기

input = list(input().split())

for word in input[1:]:
    temp = word[:-1]
    ans = input[0]
    right = 0
    for i in range(len(temp) -1, -1, -1):
        if temp[i] in "&*":
            ans += temp[i]
        elif temp[i] == "[":
            ans += "]"
        elif temp[i] == "]":
            ans += "["
        else:
            right = i
            break
    
    print(ans + " " + temp[:right+1] + ";")

# 다른 사람의 풀이 2

import sys
input = sys.stdin.readline

s = input()[:-2].replace(',', '').split()

for i in range(1, len(s)):
    if s[i].isalpha():
        print(s[0], s[i] + ';')
    else:
        for j in range(0, len(s[i])):
            if not s[i][j].isalpha():
                print(s[0] + s[i][:j - 1:-1].replace('][', '[]'), s[i][:j] + ";")
                break