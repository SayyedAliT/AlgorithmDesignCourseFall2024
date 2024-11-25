from typing import List

def calculate_reversed_strings(strings: List[str]) -> List[str]:
    return [s[::-1] for s in strings]

def initialize_dp(n: int) -> List[List[float]]:
    return [[float('inf')] * 2 for _ in range(n)]

def fill_dp_table(n: int, costs: List[int], strings: List[str], reversed_strings: List[str], dp: List[List[float]]) -> None:

    dp[0][0] = 0                  # No cost if the first string is not reversed
    dp[0][1] = costs[0]           # Cost of reversing the first string

    for i in range(1, n):
        if strings[i] >= strings[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][0])
        if strings[i] >= reversed_strings[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][1])

        if reversed_strings[i] >= strings[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][0] + costs[i])
        if reversed_strings[i] >= reversed_strings[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][1] + costs[i])

def find_min_cost(dp: List[List[float]], n: int) -> int:
    result = min(dp[n - 1][0], dp[n - 1][1])
    return result if result != float('inf') else -1

def min_magic_cost(n: int, costs: List[int], strings: List[str]) -> int:
    reversed_strings = calculate_reversed_strings(strings)
    dp = initialize_dp(n)
    fill_dp_table(n, costs, strings, reversed_strings, dp)
    return find_min_cost(dp, n)

n = int(input())
costs = list(map(int, input().split()))
strings = [input().strip() for _ in range(n)]
print(min_magic_cost(n, costs, strings))
