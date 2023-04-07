# https://www.youtube.com/watch?v=X8k48xek8g8
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()

        def dfs(r,c):
            if (r<0 or c<0 or r==rows or c==cols):
                return 0
            
            if grid[r][c]==1 or (r,c) in visited:
                return 1

            visited.add((r,c))
            return min(dfs(r+1,c),dfs(r-1,c),dfs(r,c+1),dfs(r,c-1))

        closed = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0 and (r,c) not in visited:
                    closed += dfs(r,c)
        return closed