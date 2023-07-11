# Palindromic Substring
# Have the function PalindromicSubstring(str) take the str parameter being passed and 
# find the longest palindromic substring, which means the longest substring which is read the same forwards 
# as it is backwards. For example: if str is "abracecars" then your program should return the string racecar 
# because it is the longest palindrome within the input string.

# The input will only contain lowercase alphabetic characters. The longest palindromic substring will always be unique, 
# but if there is none that is longer than 2 characters, return the string none.
# Examples
# Input: "hellosannasmith"
# Output: sannas
# Input: "abcdefgg"
# Output: none


def PalindromicSubstring(strParam):

    def recursive(strParam):
        if len(strParam) <= 1:
            return strParam

        if strParam == strParam[::-1]:
            return strParam

        left = recursive(strParam[:-1])
        right = recursive(strParam[1:])

        if len(left) >= len(right):
            return left
        else:
            return right

    longest_palindrome = recursive(strParam)
    return longest_palindrome if len(longest_palindrome) > 2 else "none"

print(PalindromicSubstring("hellosannasmith"))
print(PalindromicSubstring("abcdefgg"))
print(PalindromicSubstring("aaabc"))
print(PalindromicSubstring("aabkcdcbaa"))