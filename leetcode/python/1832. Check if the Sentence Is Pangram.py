class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {}
        for char in sentence:
            asc = ord(char)
            if asc in dic:
                dic[asc]+=1
            else:
                dic[asc]=0
        if len(dic)==26:
            return True
        return False