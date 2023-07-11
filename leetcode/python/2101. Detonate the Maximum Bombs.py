from typing import List
import math
from collections import defaultdict\

#https://www.youtube.com/watch?v=8NPbAvVXKR4&t=440s
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adjacency=defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1=bombs[i]
                x2,y2,r2=bombs[j]
                d=math.sqrt((x1-x2)**2+(y1-y2)**2)
                if d<=r1:
                    adjacency[i].append(j)
                if d<=r2:
                    adjacency[j].append(i)

        def dfs(i,visited):
            if i in visited:
                return 0
            visited.add(i)
            for neibour in adjacency[i]:
                dfs(neibour,visited)
            return len(visited)


        ans=0
        for i in range(len(bombs)):
            ans=max(ans,dfs(i,set()))
        return ans

obj = Solution()
print(obj.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))