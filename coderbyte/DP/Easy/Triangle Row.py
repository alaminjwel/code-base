# Triangle Row
# Have the function TriangleRow(num) take num which will be a positive integer representing some row from Pascal's triangle. 
# Pascal's triangle starts with a [1] at the 0th row of the triangle. Then the first row is [1, 1] and the second row is [1, 2, 1]. 
# The next row begins with 1 and ends with 1, and the inside of the row is determined by adding the k-1 and 
# kth elements from the previous row. The next row in the triangle would then be [1, 3, 3, 1], and so on. 
# The input will be some positive integer and your goal is to return the sum of that row. 
# For example: if num is 4 then your program should return the sum of 1 + 4 + 6 + 4 + 1 which is 16.
# Examples
# Input: 1
# Output: 2
# Input: 2
# Output: 4 


def TriangleRow(num):
    if num <= 1:
        return num+1

    rows = [[1], [1, 1]]
    for i in range(2, num+1):
        row = [0] * (i + 1)
        for j in range(i + 1):
            if j == 0 or j == i:
                row[j] = 1
            else:
                row[j] = rows[i-1][j-1] + rows[i-1][j]
        rows.append(row)
    return sum(rows.pop())


# Test cases
print(TriangleRow(0))  # Output: 2
print(TriangleRow(1))  # Output: 2
print(TriangleRow(2))  # Output: 4
print(TriangleRow(3))  # Output: 4
print(TriangleRow(4))  # Output: 16
