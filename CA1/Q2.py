def count_range_sum(nums, lower, upper):
    def merge_count_split_inv(start, mid, end):
        # Count sums within the specified range
        count = 0
        k = mid + 1
        j = k

        for i in range(start, mid + 1):
            while j <= end and prefix_sums[j] - prefix_sums[i] < lower:
                j += 1
            while k <= end and prefix_sums[k] - prefix_sums[i] <= upper:
                k += 1
            count += k - j

        # Merge step
        merged = []
        leftIndex = start
        rightIndex = mid + 1

        while (leftIndex <= mid and rightIndex <= end):
            if prefix_sums[leftIndex] <= prefix_sums[rightIndex]:
                merged.append(prefix_sums[leftIndex])
                leftIndex += 1
            else:
                merged.append(prefix_sums[rightIndex])
                rightIndex += 1
        while leftIndex <= mid:
            merged.append(prefix_sums[leftIndex])
            leftIndex += 1
        while rightIndex <= end:
            merged.append(prefix_sums[rightIndex])
            rightIndex += 1

        for i in range(len(merged)):
            prefix_sums[start + i] = merged[i]

        return count

    def merge_sort(start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        count = merge_sort(start, mid) + merge_sort(mid + 1, end)
        count += merge_count_split_inv(start, mid, end)
        return count

    # Calculate prefix sums
    prefix_sums = []
    prefix_sums.append(0)  # Start with the first element as 0

    # Calculate prefix sums
    for num in nums:
        prefix_sums.append(prefix_sums[-1] + num)

    # Sort the prefix sums and count valid ranges
    return merge_sort(0, len(nums))


# Example input
# Example input

    array = list(map(int, input().split()))
    lower, upper = map(int, input().split())
    # Get the result
    result = count_range_sum(array, lower, upper)
    print(result)



