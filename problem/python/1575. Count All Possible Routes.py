from typing import List
import math
from collections import defaultdict
from collections import deque

#https://leetcode.com/problems/count-all-possible-routes/solutions/3680818/python-dfs-solution-using-memoization/
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod = 10**9 +7
        memo={}
        def dfs(root,remaining):
            key=(root,remaining)
            if key in memo:
                return memo[key]

            if remaining<0:
                return 0
            
            ans=0
            if root==finish:
                ans=1
            for i in range(len(locations)):
                if root!=i:
                    ans+=dfs(i,remaining-abs(locations[i]-locations[root]))
            memo[key]=ans
            return memo[key]%mod
            
        return dfs(start,fuel)


obj = Solution()
print(obj.countRoutes([2,3,6,8,4],1,3,5))
print(obj.countRoutes([4,3,1],1,0,6))
print(obj.countRoutes([5,2,1],0,2,3))