from typing import List
import math
from typing import Optional
import queue
from collections import defaultdict

# https://www.youtube.com/watch?v=_GF-0T-YjW8
class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = [1]*n

        for i in range(n):
            if (i+1)%2==0:
                bulbs[i]=0
        
        for r in range(2,n):
            round = r+1
            if round==n:
                bulbs[-1]=1-bulbs[-1]
                break

            for i in range(0,n,round):
                if i>=round and i%round == 0:
                    bulbs[i] = 1 - bulbs[i]

        return sum(bulbs)



obj = Solution()
print(obj.bulbSwitch(4))