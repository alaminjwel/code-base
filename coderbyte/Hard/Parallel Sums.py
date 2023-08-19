# Parallel Sums
# Have the function ParallelSums(arr) take the array of integers stored in arr which will always contain an even amount of integers, and determine how they can be split into two even sets of integers each so that both sets add up to the same number. If this is impossible return -1. If it's possible to split the array into two sets, then return a string representation of the first set followed by the second set with each integer separated by a comma and both sets sorted in ascending order. The set that goes first is the set with the smallest first integer.

# For example: if arr is [16, 22, 35, 8, 20, 1, 21, 11], then your program should output 1,11,20,35,8,16,21,22
# Examples
# Input: [1,2,3,4]
# Output: 1,4,2,3
# Input: [1,2,1,5]
# Output: -1


def ParallelSums(arr):
  arr=sorted(arr)
  left,right=0,len(arr)-1
  first=True
  firstList,secondList=[],[]
  while left<=right:
    if first:
      firstList.append(arr[left])
      firstList.append(arr[right])
      first=False
    else:
      secondList.append(arr[left])
      secondList.append(arr[right])
      first=True
    left+=1
    right-=1
  if sum(firstList)==sum(secondList):
    firstList=sorted(firstList)
    secondList=sorted(secondList)
    out=",".join(str(num) for num in firstList)
    out+=","
    out+=",".join(str(num) for num in secondList)
    return out
  return -1


# keep this function call here 
print(ParallelSums(input()))


# keep this function call here 
print(ParallelSums([16,22,35,8,20,1,21,11]))