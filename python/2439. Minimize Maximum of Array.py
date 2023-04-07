#https://leetcode.com/problems/minimize-maximum-of-array/solutions/3381500/very-easy-solution-100-explained-o-n-javascript-python/
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result,total = nums[0],nums[0]
        for i in range(1,len(nums)):
            total+=nums[i]
            result = max(result,math.ceil(total/(i+1)))
        return result
