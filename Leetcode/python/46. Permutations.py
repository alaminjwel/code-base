
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(current):
            if len(current) == len(nums):
                output.append(current[:])
                return
        
            for i in nums:
                if i not in current:
                    current.append(i)
                    generate(current)
                    current.pop()
            
        output = []
        generate([])
        return output

obj = Solution()
print(obj.permute([1,2,3]))
print(obj.permute([0,1]))