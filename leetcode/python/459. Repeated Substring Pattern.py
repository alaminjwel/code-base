class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        for i in range(n-1,0,-1):
            curr = s[0:i]
            if n%len(curr)!=0:
                continue
            if curr*int(n/len(curr))==s:
                return True
        return False

obj = Solution()
print(obj.repeatedSubstringPattern("abab"))
print(obj.repeatedSubstringPattern("aba"))
print(obj.repeatedSubstringPattern("abcabcabcabc"))