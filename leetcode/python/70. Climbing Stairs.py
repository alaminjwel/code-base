class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict()
        def helper(step):
            if step in memo:
                return memo[step]
            elif step<=2:
                memo[step]=step
            else:
                memo[step]=helper(step-1)+helper(step-2)
            return memo[step]
        return helper(n)