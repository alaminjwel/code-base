# https://www.youtube.com/watch?v=lf1Pxg7IrzQ
from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(threshold):
            i,cnt = 0,0
            while i<len(nums)-1:
                if abs(nums[i]-nums[i+1])<=threshold:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
            return False

        if p==0: return 0
        nums.sort()
        l,r = 0,10**9
        res = 10**9
        while l<=r:
            m = (l+r)//2
            if isValid(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res
        

obj = Solution()
print(obj.minimizeMax([10,1,2,7,1,3],2))