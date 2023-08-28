class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        
        def solve(n, goal, dp):
            if n == 0 and goal == 0:
                return 1
            if n == 0 or goal == 0:
                return 0
            if dp[n][goal] != -1:
                return dp[n][goal]
            pick = solve(n - 1, goal - 1, dp) * n
            notpick = solve(n, goal - 1, dp) * max(n - k, 0)
            dp[n][goal] = (pick + notpick) % MOD
            return dp[n][goal]
        
        dp = [[-1] * (goal + 1) for _ in range(n + 1)]
        return solve(n, goal, dp)


obj = Solution()
print(obj.numMusicPlaylists(3, 3, 1))
print(obj.numMusicPlaylists(2, 3, 0))
print(obj.numMusicPlaylists(2, 3, 1))