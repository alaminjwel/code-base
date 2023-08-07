# https://leetcode.com/problems/search-a-2d-matrix/description/


from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        low,high = 0,col-1
        searchRow = 0
        for currRow in range(row):
            if target>=matrix[currRow][low] and target<=matrix[currRow][high]:
                searchRow = currRow
                break

        while low<=high:
            mid = (low+high)//2
            if matrix[searchRow][mid]==target:
                return True
            else:
                if matrix[searchRow][mid]>target:
                    high = mid-1
                else:
                    low = mid+1

        return False

obj = Solution()
print(obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))