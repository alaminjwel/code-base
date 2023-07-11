from typing import List
import heapq

#https://leetcode.com/problems/find-k-pairs-with-smallest-sums/solutions/3688676/lightning-fast-solution-k-pairs-with-smallest-sums-python-coding-with-vanamsen/
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        def push(i,j):
            if i<len(nums1) and j<len(nums2):
                heapq.heappush(queue,[nums1[i]+nums2[j],i,j])
        push(0,0)

        result=[]
        visited=set()
        visited.add((0,0))
        while queue and len(result)<k:
            _,i,j=heapq.heappop(queue)
            result.append([nums1[i],nums2[j]])
            if i+1<len(nums1) and (i+1,j) not in visited:
                push(i+1,j)
                visited.add((i+1,j))
            if j+1<len(nums2) and (i,j+1) not in visited:
                push(i,j+1)
                visited.add((i,j+1))
        return result


obj = Solution()
print(obj.kSmallestPairs([1,7,11],[2,4,6],3))