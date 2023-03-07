class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        s = ""
        length = max(len(a), len(b))
        for i in range(length):
            d1 = int(a[-i-1]) if i < len(a) else 0
            d2 = int(b[-i-1]) if i < len(b) else 0
            s = str(((d1 + d2 + c) % 2)) + s
            c = (d1 + d2 + c) // 2
        if (c > 0):
            s = '1' + s
        return s