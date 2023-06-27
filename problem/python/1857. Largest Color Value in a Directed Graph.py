from typing import List
from collections import defaultdict

# https://youtu.be/xLoDjKczUSk
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src,dst in edges:
            adj[src].append(dst)
        print(adj)

        def dfs(node):
            if node in currentPath: # cycle found
                return float("inf")
            if node in visited:
                return 0

            visited.add(node)
            currentPath.add(node)

            colorIndex = ord(colors[node])-ord('a')
            count[node][colorIndex] = 1

            for nei in adj[node]:
                if dfs(nei)==float("inf"):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max(
                        count[node][c],
                        (1 if c==colorIndex else 0) + count[nei][c]
                    )
            currentPath.remove(node)
            return max(count[node])

        n,res=len(colors),0
        visited,currentPath = set(),set()
        count = [[0]*26 for i in range(n)]
        for i in range(n):
            res = max(res,dfs(i))
        return -1 if res==float("inf") else res


obj = Solution()
print(obj.largestPathValue("abaca",[[0,1],[0,2],[2,3],[3,4]]))
