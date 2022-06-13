# Rod-cutting problem top down & bottom up DP solution
#
# Given n inches of rod and cut several way.
# price of rod is different by length, and maximize total revenue.

import math

def cut_rod(price):
    if len(price) == 0:
        return 0
    q = -math.inf
    for i in range(1, len(price) + 1):
        q = max(q, price[i-1] + cut_rod(price[0:len(price)-i]))
    return q

# point! buffer(revenue) list is bigger than original price list by one!

def cut_rod_DP(price, count):
    buffer = [-math.inf for _ in range(count + 1)]
    return cut_rod_DP_aux(price, count, buffer)

def cut_rod_DP_aux(price, count, buffer):
    if buffer[count] >= 0:
        return buffer[count]
    if count == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(1,count+1):
            q = max(q, price[i-1] + cut_rod_DP_aux(price, count - i, buffer))
    buffer[count] = q
    return q

def cut_rod_DP_BU(p, n):
    r = [-1] * (n+1)
    r[0] = 0
    
    for i in range(1,n+1):
        q = -math.inf
        for j in range(1,i):
            q = max(q, p[j] + r[i-j-1])
        r[i] = q
    return r[n]


# driver code

price = [1,5,8,9,10,17,17,20,24,30]
print(cut_rod(price))
print(cut_rod_DP_BU(price, len(price)))
print(cut_rod_DP(price, len(price)))