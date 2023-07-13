# Remove Brackets
# Have the function RemoveBrackets(str) take the str parameter being passed, which will contain only the characters "(" and ")", and determine the minimum number of brackets that need to be removed to create a string of correctly matched brackets. For example: if str is "(()))" then your program should return the number 1. The answer could potentially be 0, and there will always be at least one set of matching brackets in the string.
# Examples
# Input: "(())()((("
# Output: 3
# Input: "(()("
# Output: 2


def RemoveBrackets(str):
    stack = []
    count = 0

    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                count += 1

    return count + len(stack)
    
print(RemoveBrackets(input()))



# def r(s):
#   s = s.replace("()","")
#   if "()" in s:
#     s = r(s)
#   return s

# def RemoveBrackets(s):
#   return len(r(s))
  
# print(RemoveBrackets(input()))