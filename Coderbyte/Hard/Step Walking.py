# Have the function StepWalking(num) take the num parameter being passed which will be an integer between 1 and 1,000 that represents the number of stairs you will have to climb. You can climb the set of stairs by taking either 1 step or 2 steps, and you can combine these in any order. So for example, to climb 3 steps you can either do: (1 step, 1 step, 1 step) or (2, 1) or (1, 2). So for 3 steps we have 3 different ways to climb them, so your program should return 3. Your program should return the number of combinations of climbing num steps.
# Examples
# Input: 1
# Output: 1
# Input: 3
# Output: 3

def StepWalking(num):
  if num==1:
    return 1
  if num==2:
    return 2
  one = StepWalking(num-1)
  two = StepWalking(num-2)
  return one+two

# keep this function call here 
print(StepWalking(3))