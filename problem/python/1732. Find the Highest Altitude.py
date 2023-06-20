class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes=[0]
        largest=0
        for i in range(len(gain)):
            g = altitudes[i]+gain[i]
            if g>largest:
                largest=g
            altitudes.append(g)
        return largest