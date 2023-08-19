import math
from collections import defaultdict
from collections import deque
from queue import PriorityQueue
import heapq

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[i-1])
        return prefix


obj = Solution()
print(obj.runningSum([10,4,-8,7]))