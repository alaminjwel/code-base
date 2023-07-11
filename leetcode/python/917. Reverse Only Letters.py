class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left,right=0,len(s)-1
        s_list = list(s)
        while left<=right:
            l,r=s_list[left],s_list[right]
            if l.isalpha() and r.isalpha():
                s_list[left] = r
                s_list[right] = l
                left+=1
                right-=1
            elif l.isalpha():
                right-=1
            else:
                left+=1
        return ''.join(s_list)