class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive,negative=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            if nums[i]<0:
                negative+=1
            else:
                positive+=1
        return max(positive,negative)
