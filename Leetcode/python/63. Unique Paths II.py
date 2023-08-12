from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def dfs(row,col):
            key = (row,col)
            if row>m-1 or col>n-1:
                return 0
            if obstacleGrid[row][col]==1:
                return 0
            if row==m-1 and col==n-1:
                return 1
            if key in memo:
                return memo[key]

            memo[key] = dfs(row+1,col) + dfs(row,col+1)
            return memo[key]

        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return dfs(0,0)


obj = Solution()
print(obj.uniquePathsWithObstacles([[0,1],[0,0]]))