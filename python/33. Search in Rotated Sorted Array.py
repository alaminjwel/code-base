class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target:
            return 0
        low, high = 0, len(nums) - 1
        while low <= high:
            isRotated = False if nums[low] <= nums[high] else True
            mid = (low + high) // 2
            midNumber = nums[mid]
            if nums[mid] == target:
                return mid

            # If the list is not rotated then its sorted (traditional binary search)
            if not isRotated:
                if midNumber < target:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                # If left half is sorted and target is within it, search the left half
                if nums[low] <= nums[mid]:
                    if nums[low] <= target <= nums[mid - 1]:
                        high = mid - 1
                    else:
                        low = mid + 1

                # If right half is sorted and target is within it, search the right half
                elif nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1