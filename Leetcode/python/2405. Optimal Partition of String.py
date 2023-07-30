# https://leetcode.com/problems/optimal-partition-of-string/solutions/3381032/python-unique-character-substring-partitioning-on/
class Solution:
    def partitionString(self, s: str) -> int:
        currentSubStr = ""
        uniqueCharSet = set()
        subStrList = []
        for ch in s:
            if ch not in uniqueCharSet:
                currentSubStr += ch
                uniqueCharSet.add(ch)
            else:
                subStrList.append(currentSubStr)
                currentSubStr=ch
                uniqueCharSet = set(ch)
        if currentSubStr:
            subStrList.append(currentSubStr)
        return len(subStrList)