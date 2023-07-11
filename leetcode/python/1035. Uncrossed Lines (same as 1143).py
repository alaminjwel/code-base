class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def helper(idx1,idx2):
            key = (idx1,idx2)
            if key in memo:
                return memo[key]
            elif len(nums1)==idx1 or len(nums2)==idx2:
                memo[key] = 0
            elif nums1[idx1]==nums2[idx2]:
                memo[key] = 1+helper(idx1+1,idx2+1)
            else:
                memo[key] = max(helper(idx1+1,idx2),helper(idx1,idx2+1))
            return memo[key]
        return helper(0,0)