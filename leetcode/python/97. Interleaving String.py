# https://youtu.be/3Rw3p9LrgvE
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j):
            k=i+j
            if k == len(s3):
                return True

            key=(i,j)
            if key in memo:
                return memo[key]

            result = False
            if i < len(s1) and s1[i] == s3[k]:
                result = dfs(i + 1, j)
            if not result and j < len(s2) and s2[j] == s3[k]:
                result = dfs(i, j + 1)

            memo[key] = result
            return result

        memo = {}
        return dfs(0, 0)


obj = Solution()
print(obj.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(obj.isInterleave("a", "", "c"))






















# class Solution:
#     def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
        
#         def solve(n, goal, dp):
#             if n == 0 and goal == 0:
#                 return 1
#             if n == 0 or goal == 0:
#                 return 0
#             if dp[n][goal] != -1:
#                 return dp[n][goal]
#             pick = solve(n - 1, goal - 1, dp) * n
#             notpick = solve(n, goal - 1, dp) * max(n - k, 0)
#             dp[n][goal] = (pick + notpick) % MOD
#             return dp[n][goal]
        
#         dp = [[-1] * (goal + 1) for _ in range(n + 1)]
#         return solve(n, goal, dp)


# obj = Solution()
# print(obj.numMusicPlaylists(3, 3, 1))
# print(obj.numMusicPlaylists(2, 3, 0))
# print(obj.numMusicPlaylists(2, 3, 1))