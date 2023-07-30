class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        cols=defaultdict(list)
        for i in range(n):
            for j in range(n):
                cols[j].append(grid[i][j])
        count=0
        for i in range(n):
            for j in range(n):
                if grid[i]==cols[j]:
                    count+=1
        return count