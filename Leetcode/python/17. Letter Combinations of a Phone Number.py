from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
                
        letterMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def generate(current,index):
            if len(current)==len(digits):
                output.append("".join(current))
                return

            possibleCombinations = letterMap[digits[index]]
            for char in possibleCombinations:
                current.append(char)
                generate(current,index+1)
                current.pop()

        output = []
        generate([], 0)
        return output

    

obj = Solution()
print(obj.letterCombinations("23"))