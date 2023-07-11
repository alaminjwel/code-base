# Min Window Substring
# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters, and your goal is to determine the smallest substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. So for this example your program should return the string dae.

# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
# Examples
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse

def MinWindowSubstring(strArr):
    N = strArr[0]
    K = strArr[1]
  
    # Initialize the dictionary of frequencies of characters in K
    freq_K = {}
    for c in K:
        freq_K[c] = freq_K.get(c, 0) + 1
  
    # Initialize the window variables
    left = 0
    right = 0
    count = len(K)
    min_window = None
  
    while right < len(N):
        # Expand the window by moving the right boundary to the right
        if N[right] in freq_K:
            freq_K[N[right]] -= 1
            if freq_K[N[right]] >= 0:
                count -= 1
        right += 1
  
        # Shrink the window by moving the left boundary to the right
        while count == 0:
            if not min_window or right - left < len(min_window):
                min_window = N[left:right]
            if N[left] in freq_K:
                freq_K[N[left]] += 1
                if freq_K[N[left]] > 0:
                    count += 1
            left += 1
  
    return min_window if min_window else ""


# keep this function call here 
print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))