class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
            if columnNumber <= 26:
                return chr(columnNumber + 64)
            
            out = ""
            while columnNumber > 0:  # Change the condition to "columnNumber > 0"
                digit = (columnNumber - 1) % 26  # Subtract 1 before taking the modulo
                columnNumber = (columnNumber - 1) // 26  # Subtract 1 before division
                
                out = chr(digit + 65) + out  # Use 65 instead of 64
                
            return out


obj = Solution()
print(obj.convertToTitle(1))
print(obj.convertToTitle(28))
print(obj.convertToTitle(51))
print(obj.convertToTitle(52))
print(obj.convertToTitle(2))
print(obj.convertToTitle(701))
print(obj.convertToTitle(805))