# String Periods
# Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears. Your program should return the longest substring K, and if there is none it should return the string -1.

# For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string. Another example: if str is "abababababab" then your program should return ababab because it is the longest substring. If the input string contains only a single character, your program should return the string -1.
# Examples
# Input: "abcxabc"
# Output: -1
# Input: "affedaaffed"
# Output: -1


def StringPeriods(str):
    if len(str) == 1:
        return "-1"

    longest_substring = ""
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            substring = str[i:j]
            num_repeats = len(str) // len(substring)
            if substring * num_repeats == str and len(substring) > len(longest_substring):
                longest_substring = substring

    if len(longest_substring) > 0:
        return longest_substring
    else:
        return "-1"

# keep this function call here 
print(StringPeriods(input()))