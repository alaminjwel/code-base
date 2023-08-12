# https://youtu.be/Mjy4hd2xgrs

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(idx,value):
            key = (idx,value)
            if key in memo:
                return memo[key]

            if value>amount:
                return 0

            if value==amount:
                return 1

            if idx==len(coins):
                return 0

            memo[key] = dfs(idx+1,value) + dfs(idx,value+coins[idx])

            return memo[key]

        memo = {}
        return dfs(0,0)


obj = Solution()
print(obj.change(5,[1,2,5]))