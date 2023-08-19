class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        result = []
        n=len(nums)
        s=0
        for i in range(n):
            if i<k or i+k>=n:
                result.append(-1)
                s+=nums[i]
            else:
                if i==k:
                    for j in range(k,i+k+1):
                        s+=nums[j]
                else:
                    s-=nums[i-k-1]
                    s+=nums[i+k]
                result.append(s//(2*k+1))
        return result


# Prefix sum algorithm
# class Solution:
#     def getAverages(self, nums: List[int], k: int) -> List[int]:
#         n=len(nums)
#         prefixSum = [nums[0]]
#         for i in range(1,n):
#             prefixSum.append(nums[i]+prefixSum[-1])
#         result = []
#         s=0
#         for i in range(n):
#             if i<k or i+k>=n:
#                 result.append(-1)
#             else:
#                 prefixSumFirst = 0 if i-k-1<0 else prefixSum[i-k-1]
#                 avg = math.floor((prefixSum[i+k]-prefixSumFirst)/(2*k+1))
#                 result.append(avg)
#         return result