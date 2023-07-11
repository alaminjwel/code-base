# Arith Geo
# Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.
# Examples
# Input: [5,10,15]
# Output: Arithmetic
# Input: [2,4,16,24]
# Output: -1


def ArithGeo(arr):
    # Check if the input array is empty
    if not arr or len(arr)<3:
        return -1

    # Check if the difference between each pair of adjacent elements is consistent
    is_arithmetic = True
    diff = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != diff:
            is_arithmetic = False
            break
    if is_arithmetic:
        return "Arithmetic"

    # Check if each term after the first is multiplied by a constant ratio
    is_geometric = True
    ratio = arr[1] / arr[0]
    for i in range(1, len(arr)):
        if arr[i] / arr[i-1] != ratio:
            is_geometric = False
            break
    if is_geometric:
        return "Geometric"

    # If neither condition holds true, return -1
    return -1

# keep this function call here 
print(ArithGeo(input()))