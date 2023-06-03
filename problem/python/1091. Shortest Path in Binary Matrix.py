# https://www.youtube.com/watch?v=YnxUdAO7TAo&t=732s
from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited=set((0,0))
        queue=deque([(0,0,1)])
        direction = [(0,-1),(0,1),(-1,0),(1,0),(-1,-1),(-1,1),(1,-1),(1,1)]
        while queue:
            i,j,l = queue.popleft()
            if(min(i,j)<0 or max(i,j)>=n or grid[i][j]):
                continue
            if(i==n-1 and j==n-1):
                return l

            for di,dj in direction:
                if (i+di,j+dj) not in visited:
                    queue.append((i+di,j+dj,l+1))
                    visited.add((i+di,j+dj))
        return -1


# Your MyHashSet object will be instantiated and called as such:
obj = Solution()
print(obj.shortestPathBinaryMatrix([[0,1],[1,0]]))
print(obj.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
print(obj.shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]]))