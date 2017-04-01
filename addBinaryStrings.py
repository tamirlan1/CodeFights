# Avoid using built-in big integers to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

# Given two binary strings a and b, add them together and return the resulting string.

# Example

# For a = "1000" and b = "111", the output should be
# addBinaryStrings(a, b) = "1111";
# For a = "1" and b = "1", the output should be
# addBinaryStrings(a, b) = "10".
# Input/Output

# [time limit] 4000ms (py)
# [input] string a

# A string that can contain only 0 and 1.

# Guaranteed constraints:
# 0 ≤ a.length ≤ 105.

# [input] string b

# A string that can contain only 0 and 1.

# Guaranteed constraints:
# 0 ≤ b.length ≤ 105.

# [output] string

# The result of adding strings a and b, without any leading zeros.


def addBinaryStrings(a, b):
	numa = btoint(a)
	numb = btoint(b)
	return inttob(numa + numb)

def btoint(a):
	n = 0
	for i in range(len(a)):
		if a[-int(i)-1] == '1':
			n += 2**(int(i))
	return n

def inttob(a):
	bins = ''
	while a != 0:
		bins = str(a%2) + bins
		a = a/2
	return bins