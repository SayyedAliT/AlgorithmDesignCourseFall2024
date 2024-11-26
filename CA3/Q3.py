def is_beautiful(heights, k):
    """Check if the row of books is beautiful."""
    n = len(heights)
    for i in range(n):
        found = False
        for j in range(i + 1, min(i + k + 1, n)):
            if heights[j] < heights[i]:
                found = True
                break
        if not found:
            return False
    return True

def can_be_made_beautiful(n, k, heights):
    # Check if the row is already beautiful
    if is_beautiful(heights, k):
        return "YES"

    # Try swapping each pair of books (excluding the smallest book)
    for i in range(n - 1):  # smallest book is at index n-1
        for j in range(i + 1, n - 1):  # j < n-1 ensures smallest book is not swapped
            if heights[i] > heights[j]:  # Valid swap condition
                # Swap books at positions i and j
                heights[i], heights[j] = heights[j], heights[i]
                if is_beautiful(heights, k):
                    return "YES"
                # Swap back to restore original order
                heights[i], heights[j] = heights[j], heights[i]

    return "NO"

# Input processing
if __name__ == "__main__":
    # Read the inputs
    n, k = map(int, input().strip().split())
    heights = list(map(int, input().strip().split()))

    # Calculate and print the result
    print(can_be_made_beautiful(n, k, heights))
