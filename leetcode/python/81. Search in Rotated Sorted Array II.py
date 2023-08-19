from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1 and nums[0] == target:
            return True

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return True
            
            # Check if the low half is sorted
            if nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Check if the high half is sorted
            elif nums[low] > nums[mid]:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # If there are duplicates, move the low pointer to skip one duplicate
                low += 1

        return False

obj = Solution()
print(obj.search([2,5,6,0,0,1,2],0))
print(obj.search([2,5,6,0,0,1,2],3))
print(obj.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2))
print(obj.search([1,0,1,1,1],0))