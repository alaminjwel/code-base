class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maximumValue = 0
        for val in strs:
            if (val.isnumeric()):
                parsed = int(val)
            else:
                parsed = len(val)
            if (parsed > maximumValue):
                maximumValue = parsed
        return maximumValue