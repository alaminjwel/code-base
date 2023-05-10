class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = len(mat)
        ans = 0
        for i in range(r):
            ans += mat[i][i]
            if i!=r-i-1:
                ans += mat[i][r-i-1]
        return ans