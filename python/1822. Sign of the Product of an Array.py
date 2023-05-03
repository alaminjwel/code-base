class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        if product==0:
            return 0
        return -1 if product<0 else 1
