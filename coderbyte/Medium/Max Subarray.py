# Max Subarray
# Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the largest sum that can be formed by any contiguous subarray in the array. For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because the sum is formed by the subarray [5, -1, 7]. Adding any element before or after this subarray would make the sum smaller.
# Examples
# Input: [1, -2, 0, 3]
# Output: 3
# Input: [3, -1, -1, 4, 3, -1]
# Output: 8

def MaxSubarray(arr):
  maxSum = float("-inf")
  for i in range(len(arr)):
    curSum = arr[i]
    maxSum = max(maxSum,curSum)
    for j in range(i+1,len(arr)):
      curSum += arr[j]
      maxSum = max(maxSum,curSum)
  return maxSum

# keep this function call here 
print(MaxSubarray(input()))