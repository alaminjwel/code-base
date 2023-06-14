class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return
        low,high=0,0
        ranges=[]
        for i in range(1,len(nums)):            
            if nums[i]-1==nums[high]:
                high+=1
            else:
                string = str(nums[low])+"->"+str(nums[high]) if low!=high else str(nums[low])
                ranges.append(string)
                low=i
                high=i
        string = str(nums[low])+"->"+str(nums[high]) if low!=high else str(nums[low])
        ranges.append(string)
        return ranges