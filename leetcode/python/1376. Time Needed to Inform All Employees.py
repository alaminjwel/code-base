from typing import List
import math
from collections import defaultdict
from collections import deque

# https://youtu.be/zdBYi0p4L5Q
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacency = defaultdict(list)
        for i in range(n):
            adjacency[manager[i]].append(i)
        q=deque([(headID,0)])
        res=0
        while q:
            i,time=q.popleft()
            res = max(res,time)
            for emp in adjacency[i]:
                q.append((emp,time+informTime[i]))
        return res

       

obj = Solution()
print(obj.numOfMinutes(8,0,[-1,0,0,1,1,2,2,4],[2,3,4,0,5,0,0]))