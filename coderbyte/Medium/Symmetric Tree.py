# Symmetric Tree
# Have the function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent a binary tree, and determine if the tree is symmetric (a mirror image of itself). The array will be implemented similar to how a binary heap is implemented, except the tree may not be complete and NULL nodes on any level of the tree will be represented with a #. For example: if strArr is ["1", "2", "2", "3", "#", "#", "3"] then this tree looks like the following:



# For the input above, your program should return the string true because the binary tree is symmetric.
# Examples
# Input: ["4", "3", "4"]
# Output: false
# Input: ["10", "2", "2", "#", "1", "1", "#"]
# Output: true

def SymmetricTree(strArr):
  if (len(strArr) - 1) % 2 != 0:
    return 'false'
  
  start = 1
  stop = 3
  while stop <= len(strArr):
    if strArr[start:stop] != strArr[start:stop][::-1]:
      return 'false'

    start = stop
    stop = ((start + 1) * 2) - 1

  return 'true'
  
print(SymmetricTree(input()))