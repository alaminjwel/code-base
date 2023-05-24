class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        c = 0
        s = ""
        length = max(len(num1), len(num2))
        for i in range(length):
            d1 = int(num1[-i-1]) if i < len(num1) else 0
            d2 = int(num2[-i-1]) if i < len(num2) else 0
            s = str(((d1 + d2 + c) % 10)) + s
            c = (d1 + d2 + c) // 10
        if (c > 0):
            s = str(c) + s
        return s