class Solution:
    def subarraySum(self, nums, k):
        prefixSum = {0: 1}  # Initialize a hashmap to store cumulative sums and their frequencies.
        count = 0
        totalSum = 0
        
        for num in nums:
            totalSum += num
            if totalSum - k in prefixSum:
                count += prefixSum[totalSum - k]
            
            if totalSum in prefixSum:
                prefixSum[totalSum] += 1
            else:
                prefixSum[totalSum] = 1
        
        return count


obj = Solution()
print(obj.subarraySum([1,1,1],2))