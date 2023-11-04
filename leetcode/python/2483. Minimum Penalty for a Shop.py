class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Calculating prefix sum
        prefixSum = [0 if customers[0]=='N' else 1]
        n=len(customers)
        for i in range(1,n):
            convert = 0 if customers[i]=='N' else 1
            prefixSum.append(convert+prefixSum[-1])

        #  No need to calculate if YY..YYY or NN...NNN
        if prefixSum[-1]==n:
            return n
        if prefixSum[-1]==0:
            return 0

        # Penalty can be calculated as 
        # 'N' values before current index + 'Y' values after current index + Penalty of current index
        minIndex=0
        minPenalty=float("inf")
        for i in range(len(prefixSum)):
            nBeforeCount,yAfterCount=0,0
            nBeforeCount = i+1-prefixSum[i]
            if customers[i]=='N': # Excluding current form 'N' count
                nBeforeCount-=1
            yAfterCount = prefixSum[-1]-prefixSum[i]
            penalty = nBeforeCount+yAfterCount
            
            if customers[i]=='Y': # Calculating current index
                penalty+=1               
            if penalty<minPenalty:  # Finding the min penalty
                minPenalty=penalty
                minIndex=i

        # We need to calculate till nth hour
        lastPenalty=penalty-1 if customers[-1]=='Y' else penalty+1
        if lastPenalty<minPenalty:
            minIndex=i+1
        return minIndex


obj = Solution()
print(obj.bestClosingTime("YYNY"))
print(obj.bestClosingTime("NNNNN"))
print(obj.bestClosingTime("YYYY"))