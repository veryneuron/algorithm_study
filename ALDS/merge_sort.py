#merge sort implementation (top-down)
#
#while left < right
#split into left to middle and middle to right and apply merge sort
#after that, merge them and return sorted array
#pseudocode from wikipedia

def merge_sort (list):
    if len(list) <= 1:
        return list
    
    left_list = [x for x in list[0:len(list)//2]]
    right_list = [x for x in list[len(list)//2:len(list)]]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge(left_list, right_list)

def merge(left, right):
    result = []

    while left and right :
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    
    return result


test = [5,3,2,6,1,7,33,7,12]
print(merge_sort(test))
print(merge_sort([1,2]))
print(merge_sort([2,1]))