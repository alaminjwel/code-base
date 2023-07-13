# Moving Median
# Have the function MovingMedian(arr) read the array of numbers stored in arr which will contain a sliding window size, N, as the first element in the array and the rest will be a list of numbers. Your program should return the Moving Median for each element based on the element and its N-1 predecessors, where N is the sliding window size. The final output should be a string with the moving median corresponding to each entry in the original array separated by commas.

# Note that for the first few elements (until the window size is reached), the median is computed on a smaller number of entries. For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should output "1,2,3,5,6,6,4,3"
# Examples
# Input: [5, 2, 4, 6]
# Output: 2,3,4
# Input: [3, 0, 0, -2, 0, 2, 0, -2]
# Output: 0,0,0,0,0,0,0

# Example : [3, 1, 3, 5, 10, 6, 4, 3, 1], so N=3 and the list is now [3, 1, 3, 5, 10, 6, 4, 3, 1]
# windows:
# 1 
# 1,3
# 1,3,5
# 3,5,10
# 5,10,6
# 10,6,4
# 6,4,3
# 4,3,1
# Output : 1,2,3,5,6,6,4,3

import statistics
def MovingMedian(arr):
  N, numbers = arr[0],arr[1:]
  list_arrays = []
  for i,x in enumerate(numbers):
    if i < N:
      list_arrays.append(numbers[:i+1])
    else:
      list_arrays.append(numbers[i-N+1:i+1])

  return ",".join([str(int(statistics.median(x))) for x in list_arrays])

# keep this function call here 
print(MovingMedian(input()))