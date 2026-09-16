class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n)]

        # 0 segments -> exactly 1 way
        for i in range(n):
            dp[i][0] = 1

        for j in range(1, k + 1):
            total = 0

            for i in range(1, n):
                # Ways to form j-1 segments before i
                total = (total + dp[i - 1][j - 1]) % MOD

                # Don't end a segment at i
                # OR end a new segment at i
                dp[i][j] = (dp[i - 1][j] + total) % MOD

        return dp[n - 1][k]