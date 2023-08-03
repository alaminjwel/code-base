# https://leetcode.com/problems/subarray-product-less-than-k/
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left,curr,ans=0,1,0
        for right in range(len(nums)):
            curr *= nums[right]
            while curr>=k:
                curr //= nums[left]
                left+=1
            ans += right-left+1
        return ans