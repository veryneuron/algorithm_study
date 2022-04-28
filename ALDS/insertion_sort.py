#insertion sort implementation
#
#select a element at most left of the right array
#put that element at the right position of the left array
#when element put into the array, other left elements must "slide" <<< look like bubble sort?


def insertion(list):
    i = 0
    j = 1
    for i in range(len(list)):
        for j in range(i):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    return list

print(insertion([5,3,2,6,1,7,33,7,12]))
print(insertion([1,2]))
print(insertion([2,1]))