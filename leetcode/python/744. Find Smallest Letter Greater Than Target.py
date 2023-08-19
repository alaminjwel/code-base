class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo,hi=0,len(letters)-1
        ans=letters[0]
        while lo<=hi:
            mid=(lo+hi)//2
            if letters[mid]>target:
                hi=mid-1
                ans=letters[mid]
            else:
                lo=mid+1
        return ans;
        