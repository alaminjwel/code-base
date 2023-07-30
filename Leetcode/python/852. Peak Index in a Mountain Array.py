# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=0,len(arr)-1
        while left<right:
            mid = (left+right)//2

            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid

            if arr[mid-1]>arr[mid]:
                right = mid
            else:
                left=mid+1
        return -1