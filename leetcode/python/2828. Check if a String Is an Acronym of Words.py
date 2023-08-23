from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        make = ""
        for word in words:
            make+=word[0]
        print(make)
        return make==s

obj = Solution()
print(obj.isAcronym(["alice","bob","charlie"],"abc"))