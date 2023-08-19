# https://www.youtube.com/watch?v=DfljaUwZsOk&t=926s
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        q = deque()
        l,r=0,0
        
        while r<len(nums):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()
            
            if r+1>=k:
                out.append(nums[q[0]])
                l+=1
            r+=1
        
        return out
