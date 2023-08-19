class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def valid(i):
            if i==n:
                return True
            if i+1<n and nums[i]==nums[i+1] and valid(i+2):
                return True
            if i+2<n and nums[i]==nums[i+1]==nums[i+2] and valid(i+3):
                return True
            if i+2<n and nums[i]==nums[i+1]-1 and nums[i+1]==nums[i+2]-1 and valid(i+3):
                return True
        n=len(nums)
        return valid(0)

    def validPartition(self, nums: List[int]) -> bool:
        eq_pair = nums[0] == nums[1]
        if len(nums) == 2:
            return eq_pair

        dp = [False] * (len(nums) + 1)
        dp[0] = True
        dp[1] = False
        dp[2] = eq_pair

        for i in range(3, len(nums) + 1):
            a, b, c = nums[i - 3], nums[i - 2], nums[i - 1]
            dp[i] = (dp[i - 2] and b == c) or \
                    (dp[i - 3] and ((a == b and b == c) or (b - a == 1 and c - b == 1)))

            if not any(dp[i - 3:i]):
                break

        return dp[-1]