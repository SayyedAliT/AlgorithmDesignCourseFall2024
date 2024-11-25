def evaluateCN(n, k, mod):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator = (numerator * (n - i)) % mod
        denominator = (denominator * (i + 1)) % mod
    return (numerator * pow(denominator, mod - 2, mod)) % mod

def count_arrangements(arr):
    mod = 10**9 + 7
    n = len(arr)

    if n <= 1:
        return 1


    root = arr[0]
    left_subtree = []
    for x in arr[1:]:
        if x < root:
            left_subtree.append(x)

    right_subtree = []
    for x in arr[1:]:
        if x > root:
            right_subtree.append(x)

    left_size = len(left_subtree)
    right_size = len(right_subtree)


    left_count = count_arrangements(left_subtree)
    right_count = count_arrangements(right_subtree)


    total_ways = (evaluateCN(left_size + right_size, left_size, mod) * left_count % mod) * right_count

    return total_ways % mod


n = int(input())
arr = list(map(int, input().split()))


result = count_arrangements(arr) - 1
print(result)
