# https://www.youtube.com/watch?v=gf0zsh1FIgE
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()

        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            count = 1
            count+=dfs(r+1,c)
            count+=dfs(r-1,c)
            count+=dfs(r,c+1)
            count+=dfs(r,c-1)
            return count

        land,borderLand = 0,0
        for r in range(rows):
            for c in range(cols):
                land += grid[r][c]
                if grid[r][c]==1 and (r,c) not in visited and (r==0 or r==rows-1 or c==0 or c==cols-1):
                    borderLand += dfs(r,c)
        return land-borderLand