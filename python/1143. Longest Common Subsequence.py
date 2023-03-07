# Recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(None)
        def helper(idx1,idx2):
            if len(text1)==idx1 or len(text2)==idx2:
                return 0
            if text1[idx1]==text2[idx2]:
                return 1+helper(idx1+1,idx2+1)
            else:
                return max(helper(idx1+1,idx2),helper(idx1,idx2+1))
        return helper(0,0)


# Recursion with DP (performance is same as we used @functools.lru_cache(None) in previous solution to cache output)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def helper(idx1,idx2):
            key = (idx1,idx2)
            if key in memo:
                return memo[key]
            elif len(text1)==idx1 or len(text2)==idx2:
                memo[key] = 0
            elif text1[idx1]==text2[idx2]:
                memo[key] = 1+helper(idx1+1,idx2+1)
            else:
                memo[key] = max(helper(idx1+1,idx2),helper(idx1,idx2+1))
            return memo[key]
        return helper(0,0)