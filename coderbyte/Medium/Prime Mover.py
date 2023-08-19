# Prime Mover
# Have the function PrimeMover(num) return the numth prime number. The range will be from 1 to 10^4. For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
# Examples
# Input: 9
# Output: 23
# Input: 100
# Output: 541

def is_prime(value):
  for i in range(2,value):
    if value%i == 0:
      return False
  return True

def PrimeMover(num):
  value = 1
  prime_count = 0

  while prime_count !=num:
    value += 1
    if is_prime(value):
      prime_count += 1
  return value

print(PrimeMover(16))   # Output: 53
