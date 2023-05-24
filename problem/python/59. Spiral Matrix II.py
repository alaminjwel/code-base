# https://www.youtube.com/watch?v=BJnMZNwUk1M
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left,right=0,n
        top,bottom=0,n
        res = [[0 for _ in range(n)] for _ in range(n)]
        start=1
        while left<right and top<bottom:
            # get every i in top row
            for i in range(left,right):
                res[top][i]=start
                start+=1
            top+=1

            # get every i in right col
            for i in range(top,bottom):
                res[i][right-1]=start
                start+=1
            right-=1

            # edge case for single col or single row matrix
            if not (left<right and top<bottom):
                break

            # get every i in bottom row
            for i in range(right-1,left-1,-1):
                res[bottom-1][i]=start
                start+=1
            bottom-=1

            # get every i in left col
            for i in range(bottom-1,top-1,-1):
                res[i][left]=start
                start+=1
            left+=1
        return res