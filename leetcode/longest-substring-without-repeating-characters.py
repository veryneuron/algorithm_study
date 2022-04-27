from collections import deque


def lengthOfLongestSubstring(s: str) -> int:
    
    i = 0
    j = 0
    count = 1
        
    stk = deque([])
        
    if len(s) == 0:
        return 0
        
    while i<len(s)-1 and j<len(s):
        if s[j] not in stk:
            stk.append(s[j])
            if len(stk) > count:
                count = len(stk)       
            if j == len(s):
                stk.clear()
                i+=1
                j=i
            j += 1
        else:
            if len(stk) > count:
                count = len(stk)
            stk.clear()
            i+=1
            j=i
                    
    return count


print(lengthOfLongestSubstring("au"))