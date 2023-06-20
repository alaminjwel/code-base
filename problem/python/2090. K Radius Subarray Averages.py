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