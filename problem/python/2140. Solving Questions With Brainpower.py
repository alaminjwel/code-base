class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        def helper(idx=0):
            # using memory to avoid multiple operation on same index
            if idx in memo:
                return memo[idx]
            # recursion break condition
            if idx>=len(questions):
                memo[idx]=0
            else:
                # either we take current index or skip it, we have two choices
                take = questions[idx][0] + helper(idx+questions[idx][1]+1)
                skip=helper(idx+1)
                # we take the max of two availabe choices
                memo[idx]=max(take,skip)
            return memo[idx]
        return helper(0)