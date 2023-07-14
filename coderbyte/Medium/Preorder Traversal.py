# Preorder Traversal
# Have the function PreorderTraversal(strArr) take the array of strings stored in strArr, which will represent a binary tree with integer values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #. Your goal is to return the pre-order traversal of the tree with the elements separated by a space. For example: if strArr is ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "4", "#"] then this tree looks like the following tree:



# For the input above, your program should return the string 5 2 1 9 6 8 4 because that is the pre-order traversal of the tree.
# Examples
# Input: ["4", "1", "5", "2", "#", "#", "#"]
# Output: 4 1 2 5
# Input: ["2", "6", "#"]
# Output: 2 6


def PreorderTraversal(strArr):
    def traverse(index):
        if index >= len(strArr) or strArr[index] == "#":
            return

        # Visit the current node
        result.append(strArr[index])

        # Traverse left subtree
        traverse(2 * index + 1)

        # Traverse right subtree
        traverse(2 * index + 2)

    result = []
    traverse(0)

    for i in range(len(strArr)):
      if strArr[i] not in result and strArr[i]!='#':
        result.append(strArr[i])

    return " ".join(result)
    
print(PreorderTraversal(input()))