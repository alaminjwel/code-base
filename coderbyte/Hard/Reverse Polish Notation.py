# Reverse Polish Notation
# Have the function ReversePolishNotation(str) read str which will be an arithmetic expression composed of only integers and the operators: +,-,* and / and the input expression will be in postfix notation (Reverse Polish notation), an example: (1 + 2) * 3 would be
# 1 2 + 3 * in postfix notation. Your program should determine the answer for the given postfix expression. For example: if str is 2 12 + 7 / then your program should output 2.
# Examples
# Input: "1 1 + 1 + 1 +"
# Output: 4
# Input: "4 5 + 2 1 + *"
# Output: 27


def ReversePolishNotation(strParam):
	exp = strParam.split()
	stack=[]
	for i in range(len(exp)):
		if exp[i].isdigit():
			stack.append(int(exp[i]))
		else:
			op1=stack.pop()
			op2=stack.pop()
			if exp[i]=='+':
				out = op2+op1
			elif exp[i]=='-':
				out = op2-op1
			elif exp[i]=='*':
				out = op2*op1
			else:
				out = op2/op1
			stack.append(out)
	return out



print(ReversePolishNotation("4 5 + 2 1 + *"))