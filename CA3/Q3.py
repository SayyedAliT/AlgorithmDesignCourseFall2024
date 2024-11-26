def is_beautiful(arr, k):
    n = len(arr)
    for i in range(n-k):
        found = False
        for j in range(i + 1, min(i + k + 1, n)):
            if arr[j] <= arr[i]:
                found = True
                break
        if not found:
            return False
    return True
def can_be_beautiful(n, k, heights):
    for i in range(n):
        valid = False
        for j in range(i + 1, min(i + k + 1, n)):
            if heights[j] < heights[i]:
                valid = True
                break
        if not valid:
            can_swap = False
            for x in range(i + 1, min(i + k + 1, n)):  # First range: within [i+1, i+k]
                for y in range(i + k + 1, n):  # Second range: after [i+k]
                    if heights[x] > heights[y]:  # Swap condition
                        heights[x], heights[y] = heights[y], heights[x]
                        if is_beautiful(heights,k):
                            can_swap = True
                        heights[x], heights[y] = heights[y], heights[x]  # Undo swap
                        if can_swap:
                            break
                if can_swap:
                    break
            if not can_swap:
                return "NO"
            else:
                return "YES"
    return "YES"

# Reading input
n, k = map(int, input().split())
heights = list(map(int, input().split()))

# Solve and output the result
print(can_be_beautiful(n, k, heights))
