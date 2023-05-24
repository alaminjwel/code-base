class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = int("".join(str(d) for d in num)) + k
        return [int(d) for d in str(res)]