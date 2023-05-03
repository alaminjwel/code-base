# https://www.youtube.com/watch?v=bUr8cNWI09Q
# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        memo = {}
        def lcs(i,j):
            key = (i,j)
            if key in memo:
                return memo[key]
            elif i==len(s) or j==len(s2):
                memo[key] = 0
            elif s[i]==s2[j]:
                memo[key] = 1+lcs(i+1,j+1)
            else:
                memo[key] = max(lcs(i+1,j),lcs(i,j+1))
            return memo[key]
        return lcs(0,0)