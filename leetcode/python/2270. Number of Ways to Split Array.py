from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[i-1])

        ans=0
        for i in range(len(nums)-1):
            left = prefix[i]
            right = prefix[-1]-left
            if left>=right:
                ans+=1
        return ans


obj = Solution()
print(obj.waysToSplitArray([10,4,-8,7]))