def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9+7
        memo = {}
        def helper(length):
            if length>high:
                return 0
            if length in memo:
                return memo[length]
            memo[length] = 1 if length>=low else 0
            memo[length] += helper(length+zero) + helper(length+one)
            return memo[length]%mod     
        return helper(0)