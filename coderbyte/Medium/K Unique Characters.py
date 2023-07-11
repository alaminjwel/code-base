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

def KUniqueCharacters(str):
    # Get the value of k from the first character of the string
    k = int(str[0])
  
    # Initialize variables to keep track of the longest substring and its length
    longest_substring = ''
    max_length = 0
  
    # Loop through all possible substrings of str
    for i in range(2, len(str)+1):
        for j in range(i-k, 0, -1):
            substring = str[j:i]
            unique_chars = len(set(substring))
            if unique_chars == k and len(substring) > max_length:
                longest_substring = substring
                max_length = len(substring)
          
    # Return the longest substring with k unique characters
    return longest_substring

# Test cases
print(KUniqueCharacters("3aabacbebebe"))  # Output: "cbebebe"
print(KUniqueCharacters("2aabbcbbbadef"))  # Output: "bbcbbb"

