class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLength = min(len(word1),len(word2))
        result = ""
        for i in range(minLength):
            result += word1[i]+word2[i]       
        result += word1[i+1:]
        result += word2[i+1:]
        return result