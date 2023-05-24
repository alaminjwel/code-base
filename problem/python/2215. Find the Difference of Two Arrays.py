class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set([value for value in nums1 if value not in nums2])),list(set([value for value in nums2 if value not in nums1]))]


