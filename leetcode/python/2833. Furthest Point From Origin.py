class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:            
        count = {'L':0,'R':0,'_':0}
        for ch in moves:
            count[ch]+=1

        out = 0
        if count['L']>=count['R']:
            out = count['L']+count['_']-count['R']
        else:
            out = count['R']+count['_']-count['L']
        return out

obj = Solution()
print(obj.furthestDistanceFromOrigin("L_RL__R"))
print(obj.furthestDistanceFromOrigin("_R__LL_"))
print(obj.furthestDistanceFromOrigin("_______"))