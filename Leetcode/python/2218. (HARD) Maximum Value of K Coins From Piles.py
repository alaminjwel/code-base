class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        # Compute the total value of coins that can be collected from the first j coins of pile i
        pile_values = [[0] * (len(p)+1) for p in piles]
        for i in range(n):
            for j in range(1, len(piles[i])+1):
                pile_values[i][j] = pile_values[i][j-1] + piles[i][j-1]

        # Initialize the dynamic programming table
        dp = [[0] * (k+1) for _ in range(n+1)]

        # Fill the dynamic programming table
        for i in range(1, n+1):
            for j in range(1, k+1):
                for x in range(min(j, len(piles[i-1]))+1):
                    dp[i][j] = max(dp[i][j], dp[i-1][j-x] + pile_values[i-1][x])

        # Return the final result
        return dp[n][k]