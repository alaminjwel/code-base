import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        while k>0:
            popped = -heapq.heappop(heap)
            k-=1
        return popped

obj = Solution()
print(obj.findKthLargest([3,2,1,5,6,4],2))
print(obj.findKthLargest([3,2,3,1,2,4,5,5,6],4))