def min_energy(queue, left, right, A, B):
    length = right - left + 1
    total_people = sum(queue[left:right + 1])

    # Calculate energy for managing this segment directly
    if total_people == 0:
        direct_energy = A
    else:
        direct_energy = B * total_people * length

    # If the segment can be split
    if length > 1:
        mid = (left + right) // 2
        split_energy = min_energy(queue, left, mid, A, B) + min_energy(queue, mid + 1, right, A, B)
        return min(direct_energy, split_energy)

    # Return the direct energy if segment length is 1
    return direct_energy




if __name__ == "__main__":
    n, k, A, B = map(int, input().split())

    positions = list(map(int, input().split()))
    queue_length =  2**n
    queue = [0] * queue_length
    for pos in positions:
        queue[pos - 1] += 1

    print(min_energy(queue, 0, queue_length - 1, A, B))


