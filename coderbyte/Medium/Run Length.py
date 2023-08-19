# Run Length
# Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.
# Examples
# Input: "aabbcde"
# Output: 2a2b1c1d1e
# Input: "wwwbbbw"
# Output: 3w3b1w


def RunLength(strParam):
	out=""
	count=1
	for i in range(1,len(strParam)):
		if strParam[i]==strParam[i-1]:
			count+=1
		else:
			out+=str(count)+strParam[i-1]
			count=1
	out +=  str(count)+strParam[len(strParam) - 1]
	return out

print(RunLength("wwwbbbw"))