# https://chatgpt.com/c/672ef465-f22c-800f-8cdb-ea3938764c12
# i wrote a code. i except you to convert it into functions: it not considered some limits
#
# def probability_of_safe_score(n, m, k):
#     if m ==  0:
#         return 1.0
#     if n < m:
#         return 0.0
#
#     dp = [0.0] * (n + 1)
#     dp[0] = 1.0  # Start with a probability of 1 at score 0
#
#
#     for x in range(1, n + 1):
#         for i in range(min(x, k),0,-1):
#             if x - i >= m:
#                 break
#             if x - i >= 0:
#                 dp[x] += dp[x-i] / k
#
#     result = sum(dp[m:n + 1])
#     return result
#
#
# n, m, k = map(int, input().split())
# print(f"{probability_of_safe_score(n, m, k):.6f}")

def initialize_dp(n):
    dp = [0.0] * (n + 1)
    dp[0] = 1.0  # Probability of 1 at score 0
    return dp

def update_dp(dp, n, m, k):
    for x in range(1, n + 1):
        for i in range(min(x, k), 0, -1):
            if x - i >= m:
                break
            if x - i >= 0:
                dp[x] += dp[x - i] / k
    return dp

def calculate_probability(dp, m, n):
    return sum(dp[m:n + 1])

def probability_of_safe_score(n, m, k):
    if m == 0:
        return 1.0
    if n < m:
        return 0.0

    dp = initialize_dp(n)
    dp = update_dp(dp, n, m, k)
    return calculate_probability(dp, m, n)


# Example usage
n, m, k = map(int, input().split())
print(f"{probability_of_safe_score(n, m, k):.6f}")
