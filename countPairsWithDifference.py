# Given an array a of positive integers, find the number of pairs of integers for which the difference between the two numbers is equal to a given number k. Since the number of pairs could be quite large, take it modulo 109 + 7 for your output.

# Example

# For k = 3 and a = [1, 6, 8, 2, 4, 9, 12], the output should be
# countPairsWithDifference(k, a) = 3.

# There are three pairs of integers whose difference is equal to 3: (1, 4), (6, 9) and (9, 12).

# Input/Output

# [time limit] 4000ms (py)
# [input] integer k

# The specified difference between two numbers.

# Guaranteed constraints:
# 1 ≤ k ≤ 1000.

# [input] array.integer a

# Guaranteed constraints:
# 1 ≤ a.length ≤ 105,
# 1 ≤ a[i] ≤ 1000.

# [output] integer

# The number of pairs of integers with difference k modulo 109 + 7.

def countPairsWithDifference(k, a):
	a = sorted(a)
	c = 0
	i = 0
	j = 0
	lena = len(a)
	while(i < lena):
		if a[i] - a[j] == k:
			# print a[i], a[j]
			d1 = 1
			d2 = 1
			while True:
				if i+1 < lena and a[i+1] == a[i]:
					i += 1
					d1 += 1
				elif a[j+1] == a[j]:
					j += 1
					d2 += 1
				else:
					i += 1
					j += 1
					c += d1*d2
					break
			
		elif a[i] - a[j] > k:
			j += 1
		else:
			i += 1
	return c%(10**9 + 7)