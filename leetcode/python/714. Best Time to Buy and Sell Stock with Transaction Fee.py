class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        def choices(i,isBought):
            key =(i,isBought)
            if i >= len(prices):
                return 0
            if key in memo:
                return memo[key]

            if isBought: # either we can sell or skip the day
                sellProfit = prices[i] - fee + choices(i+1,False)
                skipProfit = choices(i+1,True)
                maxProfit = max(sellProfit,skipProfit)
                
            else: # either we can buy or skip the day
                buyProfit = -prices[i] + choices(i+1,True)
                skipProfit = choices(i+1,False)
                maxProfit = max(buyProfit,skipProfit)
            memo[key]=maxProfit
            return maxProfit

        return choices(0,False)