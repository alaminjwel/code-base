class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start=format(start,'b')
        goal=format(goal,'b')
        x=max(len(start),len(goal))

        for i in range(x-len(start)):
            start='0'+start
        for i in range(x-len(goal)):
            goal='0'+goal

        res=0
        for i in range(x):
            if goal[i]!=start[i]:
                res+=1
        return res