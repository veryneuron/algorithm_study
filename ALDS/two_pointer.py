# two pointer technique implementation
#
# i start from smallest value, j start from biggest value
# if criteria is bigger than sum, i++
# else, j--
# because array is ordered, don't have to find add combinations

def isPairSum(array, criteria):
    i = 0 
    j = len(array) - 1

    if j == 0:
        return False

    while i != j:
        if array[i] + array[j] == criteria:
            return True
        elif array[i] + array[j] < criteria:
            i += 1
        else:
            j -= 1
    return False

arr = [2, 3, 5, 8, 9, 10, 11]
val = 17
 
print(isPairSum(arr, val))