# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/solutions/3978515/simple-solution-beginner-friendly-easy-to-understand/
from typing import List

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n=len(nums)
        prev=nums[-1]
        ans=0
        for i in range(n-2,-1,-1):
            numOp = nums[i]//prev
            if nums[i]%prev!=0:
                numOp +=1
                prev = nums[i]//numOp
            ans+=numOp-1
        return ans




obj = Solution()
print(obj.minimumReplacement([3,10,3]))