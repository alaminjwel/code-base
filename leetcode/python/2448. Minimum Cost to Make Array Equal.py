class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        # Function to calculate the total cost for a given mid value
        def calCost(mid):
            costNum = 0
            for i in range(len(nums)):
                # Accumulate the cost by taking the absolute difference multiplied by the corresponding cost
                costNum += abs(nums[i] - mid) * cost[i]
            return costNum

        left, right = min(nums), max(nums)

        # Perform binary search
        while left < right:
            mid = (left + right) // 2

            if calCost(mid) < calCost(mid + 1):
                # If the cost for mid is less, we will search in first half
                right = mid
            else:
                # Otherwise, we will search in second half
                left = mid + 1
        return calCost(left)