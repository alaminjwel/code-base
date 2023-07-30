class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mul = 0
        for i in range(len(num1)):
            st = ""
            ct = 0
            for j in range(len(num2)):
                d1 = int(num1[-i-1] or 0)
                d2 = int(num2[-j-1] or 0)
                st = str((((d1 * d2) + ct) % 10)) + st
                ct = ((d1 * d2) + ct) // 10
            if (ct > 0): st = str(ct) + st
            mul += int(st) * 10**i
        return str(mul)