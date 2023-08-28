from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        sortedPairs = sorted(pairs, key=lambda x: x[1])# Sort by the second element
        print(sortedPairs)
        count=1
        lastPair=0
        for curPair in range(1,len(sortedPairs)):
            a,b=sortedPairs[lastPair]
            c,d=sortedPairs[curPair]
            if b<c:
                count+=1
                lastPair=curPair
        return count



obj = Solution()
print(obj.findLongestChain([[1,2],[2,3],[3,4]]))
print(obj.findLongestChain([[1,2],[7,8],[4,5]]))
print(obj.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))





















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