class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=['a','e','i','o','u']
        count=0
        # Find vowels count in first window
        for c in s[:k]:
            if c in vowels:
                count+=1
        maxCount = count

        # Find vowels count in rest windows
        for i in range(k,len(s)):
            if s[i-k] in vowels:
                count-=1
            if s[i] in vowels:
                count+=1
            maxCount = max(count,maxCount)
        return maxCount

