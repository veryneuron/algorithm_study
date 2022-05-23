#bubble sort implementation
#
#start from left, keep exchange to right positon

def bubble(list):
    for i in range(len(list))[::-1]:
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubble([5,3,2,6,1,7,33,7,12]))
print(bubble([1,2]))
print(bubble([2,1]))