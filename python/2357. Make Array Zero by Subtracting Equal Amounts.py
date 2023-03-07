#check the problem hint
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if (nums[i] > 0):
                freq[nums[i]] = freq.get(nums[i], 0) + 1
        return len(freq)