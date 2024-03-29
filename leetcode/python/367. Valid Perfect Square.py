class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo,hi=1,num
        while lo<=hi:
            mid=(lo+hi)//2
            if mid*mid==num:
                return True
            if mid*mid>num:
                hi=mid-1
            else:
                lo=mid+1
        return False
