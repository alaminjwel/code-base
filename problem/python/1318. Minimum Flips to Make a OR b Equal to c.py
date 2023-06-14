class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        abin=format(a,'b')
        bbin=format(b,'b')
        cbin=format(c,'b')
        x = max(len(abin),len(bbin),len(cbin))
        for i in range(x-len(abin)):
            abin="0"+abin
        for i in range(x-len(bbin)):
            bbin="0"+bbin
        for i in range(x-len(cbin)):
            cbin="0"+cbin
        res=0
        for i in range(x):
            if cbin[i]=='1':
                if abin[i]=='0' and bbin[i]=='0':
                    res+=1
            else:
                if abin[i]=='1' :
                    res+=1
                if bbin[i]=='1' :
                    res+=1
        return res