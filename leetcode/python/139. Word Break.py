from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(st, dic, memo):
            if not st:
                return True
            if st in memo:
                return memo[st]
            for word in dic:
                if st.startswith(word):
                    new_st = st.replace(word, "", 1)
                    if helper(new_st, dic, memo):
                        memo[st] = True
                        return True
            memo[st] = False
            return False

        memo = {}
        return helper(s, wordDict, memo)

obj = Solution()
print(obj.wordBreak("leetcode",["leet","code"]))
# print(obj.wordBreak("catsandog",["cats","dog","sand","and","cat"]))
# print(obj.wordBreak("cars",["car","ca","rs"]))
# print(obj.wordBreak("aaaaaaab",["aaaa","aaa","b"]))