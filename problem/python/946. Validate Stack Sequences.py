class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i=0
        for n in pushed:
            stk.append(n)
            while i<len(popped) and stk and popped[i]==stk[-1]:
                stk.pop()
                i+=1
        return not stk