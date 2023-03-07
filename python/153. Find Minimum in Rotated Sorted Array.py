class Solution:
    def findMin(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        lo = 0
        hi = len(nums)-1

        if nums[lo] <= nums[hi]:
            return nums[0]

        while lo <= hi:
            mid = (lo+hi)//2
            mid_number = nums[mid]

            if mid > 0 and mid_number < nums[mid-1]:
                return nums[mid]

            elif mid_number < nums[hi]:
                hi = mid - 1

            else:
                lo = mid + 1

        return nums[lo]