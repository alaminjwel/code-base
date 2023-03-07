class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low) // 2
        if(high % 2 == 1 or low % 2 == 1):
            odds += 1
        return odds
