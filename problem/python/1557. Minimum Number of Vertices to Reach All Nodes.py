from typing import List
from typing import Optional
from collections import defaultdict

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = [False for _ in range(n)]
        destination = [] 
        for i in range(len(edges)):
            destination.append(edges[i][1]) # list of destination nodes
            nodes[edges[i][1]]=True # list of nodes have incoming egde
        return [node for node in range(n) if not nodes[node]] # list of nodes have no incoming egde

obj = Solution()
print(obj.findSmallestSetOfVertices(6,[[0,1],[0,2],[2,5],[3,4],[4,2]]))