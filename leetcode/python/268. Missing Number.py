from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]]=True
        left=0
        while left<len(nums):
            if dic.get(left) is None:
                return left
            left+=1
        return left

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         if not 0 in nums and len(nums)>0:
#             return 0
#         nums=sorted(nums)
#         for i in range(len(nums)): 
#             if nums[i]!=i:
#                 return i
#         return nums[-1]+1

obj = Solution()
print(obj.missingNumber([0,1]))
# print(obj.missingNumber([3,0,1]))