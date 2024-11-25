def min_magic_cost(n, costs, strings):
    # Initialize dp arrays
    dp = [[float('inf')] * 2 for _ in range(n)]

    # Reverse each string once to avoid reversing multiple times in the loop
    reversed_strings = [s[::-1] for s in strings]

    # Base cases
    dp[0][0] = 0  # No cost if the first string is not reversed
    dp[0][1] = costs[0]  # Cost of reversing the first string

    # Fill dp table
    for i in range(1, n):
        # Transition for dp[i][0] (current string not reversed)
        if strings[i] >= strings[i - 1]:  # If current string >= previous string (not reversed)
            dp[i][0] = min(dp[i][0], dp[i - 1][0])
        if strings[i] >= reversed_strings[i - 1]:  # If current string >= previous string (reversed)
            dp[i][0] = min(dp[i][0], dp[i - 1][1])

        # Transition for dp[i][1] (current string reversed)
        if reversed_strings[i] >= strings[i - 1]:  # If reversed current string >= previous string (not reversed)
            dp[i][1] = min(dp[i][1], dp[i - 1][0] + costs[i])
        if reversed_strings[i] >= reversed_strings[i - 1]:  # If reversed current string >= previous string (reversed)
            dp[i][1] = min(dp[i][1], dp[i - 1][1] + costs[i])

    # Calculate the minimum magic cost for sorting all strings
    result = min(dp[n - 1][0], dp[n - 1][1])

    # Return -1 if it's impossible to sort the strings
    return result if result != float('inf') else -1


# Example usage
n = int(input())
costs = list(map(int, input().split()))
strings = [input().strip() for _ in range(n)]
print(min_magic_cost(n, costs, strings))
