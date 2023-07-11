# String Reduction
# Have the function StringReduction(str) take the str parameter being passed and 
# return the smallest number you can get through the following reduction method. 
# The method is: Only the letters a, b, and c will be given in str and 
# you must take two different adjacent characters and replace it with the third. 
# For example "ac" can be replaced with "b" but "aa" cannot be replaced with anything. 
# This method is done repeatedly until the string cannot be further reduced, 
# and the length of the resulting string is to be outputted.

# For example: if str is "cab", then "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc"). The reduction is done so the output should be 2. If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab" reduces to "c", and the final string "ac" is reduced to "b" so the output should be 1.
# Examples
# Input: "abcabc"
# Output: 2
# Input: "cccc"
# Output: 4 


def StringReduction(strParam):
   # Base case: if the string length is 1 or 2, no further reduction is possible
    if len(strParam) == 1 or (len(strParam) == 2 and strParam[0]==strParam[1]):
        return len(strParam)
    
    # Check for adjacent characters that can be reduced
    for i in range(len(strParam) - 1):
        if strParam[i] != strParam[i+1]:
            reduced_str = strParam[:i] + get_replacement(strParam[i], strParam[i+1]) + strParam[i+2:]
            return StringReduction(reduced_str)  # Recursive call
    
    # If no reduction was possible, return the length of the string
    return len(strParam)

def get_replacement(a, b):
    # Determine the replacement character based on the given characters
    if (a == 'a' and b == 'b') or (a == 'b' and b == 'a'):
        return 'c'
    elif (a == 'a' and b == 'c') or (a == 'c' and b == 'a'):
        return 'b'
    elif (a == 'b' and b == 'c') or (a == 'c' and b == 'b'):
        return 'a'

# keep this function call here 
print(StringReduction("bcab")) #output : 1
print(StringReduction("aabc")) #output : 1
print(StringReduction("abb")) #output : 1

print(StringReduction("abcabc")) #output : 2
print(StringReduction("cccc")) #output : 4