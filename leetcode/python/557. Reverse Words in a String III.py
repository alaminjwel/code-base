class Solution:
    def reverseWords(self, s: str) -> str:
        left, right, ans = 0, 0, ""
        while right < len(s):
            if s[right] == ' ':
                ans += s[left:right][::-1] + ' '
                left = right + 1
            right += 1
        ans += s[left:right][::-1]
        return ans