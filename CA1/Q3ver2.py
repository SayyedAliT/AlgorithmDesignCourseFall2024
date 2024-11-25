def min_energy(queue, left, right, A, B, memo, prefix_sum):
    # Check if result already computed
    if (left, right) in memo:
        return memo[(left, right)]

    length = right - left + 1
    total_people = prefix_sum[right + 1] - prefix_sum[left]  # Using prefix sums

    # Calculate energy for managing this segment directly
    if total_people == 0:
        direct_energy = A
    else:
        direct_energy = B * total_people * length

    # If the segment can be split
    if length > 1:
        mid = (left + right) // 2
        split_energy = min_energy(queue, left, mid, A, B, memo, prefix_sum) + \
                       min_energy(queue, mid + 1, right, A, B, memo, prefix_sum)
        min_cost = min(direct_energy, split_energy)
    else:
        min_cost = direct_energy

    # Store the result in memo
    memo[(left, right)] = min_cost
    return min_cost


def main():
    n, k, A, B = map(int, input().split())
    queue_length = 2 ** n
    queue = [0] * queue_length

    positions = list(map(int, input().split()))
    for pos in positions:
        queue[pos - 1] += 1  # Convert to 0-based index

    # Prepare prefix sums
    prefix_sum = [0] * (queue_length + 1)
    for i in range(queue_length):
        prefix_sum[i + 1] = prefix_sum[i] + queue[i]

    # Dictionary for memoization
    memo = {}

    result = min_energy(queue, 0, queue_length - 1, A, B, memo, prefix_sum)

    print(result)


if __name__ == "__main__":
    main()
