from typing import List
from collections import defaultdict
from collections import deque
from queue import PriorityQueue

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        valid = PriorityQueue()  # Valid workers to be chosen from
        ignored = deque()  # Invalid workers those we cant choose for now
        leftTaken = 0  # Max index of taken worker from the left

        for i in range(n):
            if i < candidates: # Valid workers from the left section
                valid.put((costs[i], i))
                leftTaken += 1
            elif n - i <= candidates: # Valid workers form the right/end section
                valid.put((costs[i], i))
            else:
                ignored.append((costs[i], i))

        total = 0
        while k > 0: # Hiring k times
            c, i = valid.get()  # Get the worker with the lowest cost
            total += c

            # Add a new worker to valid list from ignored set
            if len(ignored) > 0:
                if i <= leftTaken: # The last worker we hired was from left section
                    valid.put(ignored.popleft())
                    leftTaken += 1
                else:
                    valid.put(ignored.pop())
            k -= 1
            
        return total


obj = Solution()
print(obj.totalCost([17,12,10,2,7,2,11,20,8],3,4))
print(obj.totalCost([1,2,4,1],3,3))
print(obj.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2))