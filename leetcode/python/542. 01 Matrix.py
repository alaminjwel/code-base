from queue import PriorityQueue
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        disMat = [[float('inf')] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    disMat[r][c] = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    if r > 0:
                        disMat[r][c] = min(disMat[r][c], disMat[r - 1][c] + 1)
                    if c > 0:
                        disMat[r][c] = min(disMat[r][c], disMat[r][c - 1] + 1)

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if mat[r][c] == 1:
                    if r < rows - 1:
                        disMat[r][c] = min(disMat[r][c], disMat[r + 1][c] + 1)
                    if c < cols - 1:
                        disMat[r][c] = min(disMat[r][c], disMat[r][c + 1] + 1)

        return disMat

obj = Solution()
print(obj.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
print(obj.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
print(obj.updateMatrix([[0,0,1,0,1,1,1,0,1,1],[1,1,1,1,0,1,1,1,1,1],[1,1,1,1,1,0,0,0,1,1],[1,0,1,0,1,1,1,0,1,1],[0,0,1,1,1,0,1,1,1,1],[1,0,1,1,1,1,1,1,1,1],[1,1,1,1,0,1,0,1,0,1],[0,1,0,0,0,1,0,0,1,1],[1,1,1,0,1,1,0,1,0,1],[1,0,1,1,1,0,1,1,1,0]]))



# Of course! The dynamic programming (DP) solution I provided uses a different approach to 
# solve the problem while maintaining the same idea of finding the distance of the nearest 0 
# for each cell in the binary matrix. Let me explain how the DP solution works step by step:

# Initialize the Distance Matrix: We start by initializing a disMat matrix of the 
# same size as the input matrix mat. Each cell in disMat will represent the minimum distance of the corresponding cell in mat to the nearest 0.

# Initialize Zero Cells: We iterate through the original matrix mat and for each 
# cell containing a 0, we set the corresponding cell in disMat to 0. This is because 
# the distance from a cell to itself is always 0.

# Update Distances Using DP: We perform three passes through the disMat matrix 
# to update the distances efficiently.

# a. Top-left to Bottom-right Pass: In this pass, we iterate through each cell 
# from the top-left to the bottom-right. For each cell, if it's not a 0, we update 
# its distance by taking the minimum of the distances from its top and left neighbors 
# (if they exist), and adding 1. This ensures that we consider the closest 0 cell from the top and left directions.

# b. Bottom-right to Top-left Pass: Similar to the previous pass, but we iterate 
# from the bottom-right to the top-left. For each cell, we update its distance by 
# considering the minimum of its current distance and the distances of its bottom 
# and right neighbors plus 1. This ensures we consider the closest 0 cell from the bottom and right directions.

# c. Bottom-left to Top-right Pass: This final pass goes from the bottom-left 
# to the top-right. Again, for each cell, we update its distance by considering 
# the minimum of its current distance and the distances of its bottom and left neighbors plus 1.

# Result: After completing the three passes, the disMat matrix contains the minimum 
# distances of each cell to the nearest 0. We return this matrix as the final result.

# The DP approach eliminates the need for explicit DFS traversal and memoization by 
# efficiently propagating the distances from known cells with 0 values to their neighboring cells. This approach is more efficient than DFS in terms of time complexity and avoids potential issues with infinite recursion.