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


# https://medium.com/@kevinmavani/longest-common-subsequence-using-dynamic-programming-641eed90dab1
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1,n2=len(text1),len(text2)
        results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        for idx1 in range(n1):
            for idx2 in range(n2):
                if text1[idx1] == text2[idx2]:
                    results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
                else:
                    results[idx1+1][idx2+1] = max(results[idx1][idx2+1],results[idx1+1][idx2])
        return results[-1][-1]