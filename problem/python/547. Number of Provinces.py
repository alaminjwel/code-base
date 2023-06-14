class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adjacency = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j or isConnected[i][j]==0:
                    continue
                adjacency[i].append(j)

        def dfs(node):
            visited = set()
            stack = [node]
            while stack:
                i = stack.pop()
                if i not in visited:
                    visited.add(i)
                    for neighbor in adjacency[i]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return visited

        ans = []
        for i in range(n):
            traverse = dfs(i)
            if traverse not in ans:
                ans.append(traverse)
        return len(ans)