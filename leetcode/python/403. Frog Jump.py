from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        goal = stones[-1]
        stonesSet = set(stones)
        memo = {}

        def dfs(position,jumpSize):
            key = (position,jumpSize)
            if position==goal:
                return True
            if key in memo:
                return memo[key]

            for nextJump in [jumpSize,jumpSize+1,jumpSize-1]:
                if nextJump>0 and (position+nextJump) in stonesSet:
                    if dfs(position+nextJump,nextJump):
                        memo[key]=True
                        return True
            memo[key]=False
            return False

        return dfs(0,0)


obj = Solution()
print(obj.canCross([0,1,3,5,6,8,12,17]))
print(obj.canCross([0,1,2,3,4,8,9,11]))

