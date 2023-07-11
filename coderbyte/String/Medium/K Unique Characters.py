# K Unique Characters
# Have the function KUniqueCharacters(str) take the str parameter being passed and 
# find the longest substring that contains k unique characters, where k will be the first character from the string. 
# The substring will start from the second position in the string because the first character will be the integer k. 
# For example: if str is "2aabbacbaa" there are several substrings that all contain 2 unique characters, 
# namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba" because it is the longest substring. 
# If there are multiple longest substrings, then return the first substring encountered with the longest length. k will range from 1 to 6.

# Examples
# Input: "3aabacbebebe"
# Output: cbebebe
# Input: "2aabbcbbbadef"
# Output: bbcbbb 


from collections import defaultdict

def KUniqueCharacters(strParam):
    k = int(strParam[0])  # Extract the value of k from the first character
    strParam = strParam[1:]  # Remove the first character from the string
    longest_substring = ""  # Variable to store the longest substring
    max_length = 0  # Variable to store the length of the longest substring
    substring_counts = defaultdict(int)  # Dictionary to track the count of characters in the window
    unique_count = 0  # Variable to track the number of unique characters in the window
    start = 0  # Pointer to represent the start of the current window

    for end in range(len(strParam)):
        substring_counts[strParam[end]] += 1

        if substring_counts[strParam[end]] == 1:
            unique_count += 1

        while unique_count > k:
            substring_counts[strParam[start]] -= 1
            if substring_counts[strParam[start]] == 0:
                unique_count -= 1
            start += 1

        substring_length = end - start + 1
        if unique_count == k and substring_length > max_length:
            max_length = substring_length
            longest_substring = strParam[start:end+1]

    return longest_substring

# Test cases
print(KUniqueCharacters("3aabacbebebe"))  # Output: "cbebebe"
print(KUniqueCharacters("2aabbcbbbadef"))  # Output: "bbcbbb"

