def calculate_probability(n, m, k, dp, x):
    return sum(
        dp[x - i] / k
        for i in range(min(x, k), 0, -1)
        if x - i >= 0 and x - i < m
    )

def generate_dp_values(n, m, k):
    # Base case: probability of 1 at score 0
    dp = [1.0] + [0.0] * n
    return [dp[0]] + [calculate_probability(n, m, k, dp[:x], x) for x in range(1, n + 1)]

def probability_of_safe_score(n, m, k):
    if m == 0:
        return 1.0
    if n < m:
        return 0.0

    dp = generate_dp_values(n, m, k)
    return sum(dp[m:n + 1])

# Example usage
n, m, k = map(int, input().split())
print(f"{probability_of_safe_score(n, m, k):.6f}")
