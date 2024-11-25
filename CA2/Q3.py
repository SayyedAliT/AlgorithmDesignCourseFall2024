MOD = 10**8

def initialize_dp(n, m):
    return [[[0 for _ in range(2)] for _ in range(m + 1)] for _ in range(n + 1)]

def set_base_cases(dp, n, m, v, c):
    for i in range(1, v + 1):
        if i <= n:
            dp[i][0][0] = 1
    for i in range(1, c + 1):
        if i <= m:
            dp[0][i][1] = 1

def fill_dp(dp, n, m, v, c):
    for i in range(n + 1):
        for j in range(m + 1):
            if i > 0:
                for k in range(1, v + 1):
                    if i >= k:
                        dp[i][j][0] += dp[i - k][j][1]
                        dp[i][j][0] %= MOD
            if j > 0:
                for k in range(1, c + 1):
                    if j >= k:
                        dp[i][j][1] += dp[i][j - k][0]
                        dp[i][j][1] %= MOD

def count_symbolic_arrangements(n, m, v, c):
    dp = initialize_dp(n, m)
    set_base_cases(dp, n, m, v, c)
    fill_dp(dp, n, m, v, c)
    return (dp[n][m][0] + dp[n][m][1]) % MOD

n, m, v, c = map(int, input().split())
print(count_symbolic_arrangements(n, m, v, c))
    