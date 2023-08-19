from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right,maxLen,countZero=0,0,0,0
        for right in range(len(nums)):
            if nums[right]==0:
                countZero+=1          
            while countZero>k:
                if nums[left]==0:
                    countZero-=1
                left += 1
            winSize = right-left+1
            maxLen = max(maxLen,winSize)
        return maxLen


obj = Solution()
print(obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
print(obj.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))
print(obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))