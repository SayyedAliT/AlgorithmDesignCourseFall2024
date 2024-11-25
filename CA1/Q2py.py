def count_range_sum(nums, lower, upper):
    def count_and_merge(start, mid, end):
        # Count sums within the specified range
        total_count = 0
        right_bound = mid + 1
        lower_bound = right_bound

        for left_index in range(start, mid + 1):
            while lower_bound <= end and prefix_sums[lower_bound] - prefix_sums[left_index] < lower:
                lower_bound += 1
            while right_bound <= end and prefix_sums[right_bound] - prefix_sums[left_index] <= upper:
                right_bound += 1
            total_count += right_bound - lower_bound

        # Merge step to combine the two halves
        merged_sums = []
        left_ptr = start
        right_ptr = mid + 1

        while left_ptr <= mid and right_ptr <= end:
            if prefix_sums[left_ptr] <= prefix_sums[right_ptr]:
                merged_sums.append(prefix_sums[left_ptr])
                left_ptr += 1
            else:
                merged_sums.append(prefix_sums[right_ptr])
                right_ptr += 1
        while left_ptr <= mid:
            merged_sums.append(prefix_sums[left_ptr])
            left_ptr += 1
        while right_ptr <= end:
            merged_sums.append(prefix_sums[right_ptr])
            right_ptr += 1

        for i in range(len(merged_sums)):
            prefix_sums[start + i] = merged_sums[i]

        return total_count

    def divide_and_conquer(start, end):
        if start >= end:
            return 0
        mid = (start + end) // 2
        count = divide_and_conquer(start, mid) + divide_and_conquer(mid + 1, end)
        count += count_and_merge(start, mid, end)
        return count

    # Calculate prefix sums
    prefix_sums = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]

    # Count valid ranges
    return divide_and_conquer(0, len(nums))


# Example input
if __name__ == "__main__":
    array = list(map(int, input().split()))
    lower, upper = map(int, input().split())
    # Get the result
    result = count_range_sum(array, lower, upper)
    print(result)
