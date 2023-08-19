class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0
        while left<len(nums) and right<len(nums):
            if nums[right]!=0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
            right+=1