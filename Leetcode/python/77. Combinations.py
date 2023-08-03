# https://leetcode.com/problems/combinations/

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def generate(current, start):
            if len(current) == k:
                output.append(current[:])
                return
                
            for i in range(start, n + 1):
                current.append(i)
                generate(current, i + 1)
                current.pop()

        output = []
        generate([], 1)
        return output

obj = Solution()
print(obj.combine(3,3))
print(obj.combine(1,1))
print(obj.combine(4,1))
print(obj.combine(4,2))