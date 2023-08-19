class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start=1
        while True:
            curr = start
            prefix=[]
            invalid = False
            for i in range(0,len(nums)):
                curr+=nums[i]
                prefix.append(curr)
            validCount = 0
            for i in prefix:
                if i>=1:
                    validCount+=1
                else:
                    break
            if validCount==len(prefix):
                return start
            start+=1


# Chat GPT Better Solution
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_prefix_sum = float('inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            min_prefix_sum = min(min_prefix_sum, curr_sum)

        return max(1, 1 - min_prefix_sum)