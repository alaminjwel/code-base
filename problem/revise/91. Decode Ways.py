class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = [-1 for _ in range(len(s) + 1)]
        
        def recurse(i, s):
            if i > len(s) - 1:
                return 1

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = 0
            for j in [1, 2]:
                # the order of this condition checking is important
                if i + j <= len(s) and s[i] != "0" and 0 < int(s[i:i+j]) < 27:
                    memo[i] += recurse(i+j, s)

            return memo[i]

        return recurse(0, s)