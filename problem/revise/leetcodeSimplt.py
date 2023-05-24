from typing import List
import math
from typing import Optional
import queue
from collections import defaultdict

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s
        return num
             
        
obj = Solution()
print(obj.addDigits(38))