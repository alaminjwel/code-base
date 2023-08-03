# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/solutions/3841328/recursive-memoization-intuitive-solution/

from typing import List

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # function that find ASCII sum of a string
        def getAsciiSum(string):
            ascii_sum = 0
            for char in string:
                ascii_sum += ord(char)
            return ascii_sum

        # fining longest common subsequence based on ASCII sum
        memo = {}
        def helper(idx1,idx2):
            key = (idx1,idx2)

            if idx1==len(s1) or idx2==len(s2): # no more char left
                memo[key]=""
            elif key in memo: # already computed previously
                return memo[key]

            elif s1[idx1]==s2[idx2]: # found a match, return the common char
                memo[key]=s1[idx1]+helper(idx1+1,idx2+1)

            else: # we have two choices, skip first or skip second
                choice1 = helper(idx1+1,idx2)
                choice2 = helper(idx1,idx2+1)
                if len(choice1)==len(choice2): # the choices are equal, we will take the one having larger ASCII sum
                    ascii1=getAsciiSum(choice1)
                    ascii2=getAsciiSum(choice2)
                    memo[key] = choice1 if ascii1>ascii2 else choice2
                else: # take the one which is larger
                    memo[key] = choice1 if len(choice1)>len(choice2) else choice2
            return memo[key]

        longestCommonAsciiSubsequence = helper(0,0)

        # removing longest common subsequence from both inputs
        for c in longestCommonAsciiSubsequence:
            s1 = s1.replace(c, "", 1)        
        for c in longestCommonAsciiSubsequence:
            s2 = s2.replace(c, "", 1)

        # getting the ASCII sum of left over inputs
        return getAsciiSum(s1) + getAsciiSum(s2)        

obj = Solution()
print(obj.minimumDeleteSum("sea","eat"))
print(obj.minimumDeleteSum("delete","leet"))
