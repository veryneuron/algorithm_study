# prefix sum implementation

def prefix_sum(arr):
    result = []
    result.append(arr[0])
    for i in range(1,len(arr)):
        result.append(result[i-1] + arr[i])
    return result

print(prefix_sum([10,4,16,20]))