from typing import List
import math
# from typing import Optional
# import queue

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        found = 0

        for i in range(0,n):
            s = nums[i]

            if s==k:                    
                found += 1

            for j in range(i+1,n+1):

                if j<n:
                    if math.isinf(s) and s < 0:
                        s = 0
                    s += nums[j]

                    if s==k:                    
                        found += 1
        return found



obj = Solution()
print(obj.subarraySum([1,1,1],1))
