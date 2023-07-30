class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = len(s)
        pointS,pointT = 0,0
        while pointS<len(s) and pointT<len(t):
            if s[pointS] == t[pointT]:
                count-=1
                pointS+=1
            pointT+=1
        return count==0
