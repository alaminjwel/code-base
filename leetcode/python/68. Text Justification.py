from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        def createLine(curLineWords, curLineLength):            
            totalSpaces = maxWidth - curLineLength # How many spaces we will add in total
            spacePlaces = len(curLineWords) - 1 # How many places we will add the spaces

            if spacePlaces == 0: # Just add the spaces at the right
                return curLineWords[0] + " " * totalSpaces

            spacesBetween = totalSpaces // spacePlaces # How many spaces/place to be addd
            extraSpaces = totalSpaces % spacePlaces # There may be extra space left when not evenly distributed
            
            line = curLineWords[0]
            for i in range(1, len(curLineWords)):
                if extraSpaces > 0: # Add the extra space
                    line += " " * (spacesBetween + 1)
                    extraSpaces -= 1
                else:
                    line += " " * spacesBetween
                line += curLineWords[i]
            
            return line

        result = []
        curLineWords = []  # To store the words for the current line
        curLineLength = 0  # To store the total length of words and spaces on the current line
        
        for word in words:
            # Check if the current word can fit in the current line
            if curLineLength + len(curLineWords) + len(word) > maxWidth:
                result.append(createLine(curLineWords, curLineLength))
                curLineWords = []
                curLineLength = 0
            
            curLineWords.append(word)
            curLineLength += len(word)
        
        # Handle the last line (left-justified)
        lastLine = " ".join(curLineWords)
        result.append(lastLine + " " * (maxWidth - len(lastLine)))
        
        return result


obj = Solution()
print(obj.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))