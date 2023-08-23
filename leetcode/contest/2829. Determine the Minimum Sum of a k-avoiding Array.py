from typing import List

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        count=0
        arr=[]
        s=0
        while len(arr)<n:
            count+=1
            invalid = False
            for a in arr:
                if a+count==k:
                    invalid=True
                    break
            if invalid:
                continue
            s+=count
            arr.append(count)
        return s

obj = Solution()
print(obj.minimumSum(5,4))