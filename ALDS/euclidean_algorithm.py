# euclidean algorithm(compute gcd)

def euclidean_algorithm(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

# it's woks when n1<n2 also

def euclidean_algorithm_recursive(n1, n2):
    temp = n1 % n2
    if temp == 0:
        return n2
    else:
        return euclidean_algorithm_recursive(n2, temp)

print(euclidean_algorithm(1112,695))
print(euclidean_algorithm_recursive(695,1112))