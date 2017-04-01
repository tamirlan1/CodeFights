# Avoid using built-in big integers when solving this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

# Multiply two numbers that have been given to you as strings, s1 and s2, and return the result as a string. Neither s1 nor s2 contain leading zeros, and your answer shouldn't either.

# Example

# For s1 = "15" and s2 = "3", the output should be
# multiplyTwoStrings(s1, s2) = "45";
# For s1 = "13" and s2 = "13", the output should be
# multiplyTwoStrings(s1, s2) = "169".
# Input/Output

# [time limit] 4000ms (py)
# [input] string s1

# Guaranteed constraints:

# 1 ≤ s1.length ≤ 1000.

# [input] string s2

# Guaranteed constraints:

# 1 ≤ s2.length ≤ 1000.

# [output] string

# The result of s1 * s2, without a leading zero.

def multiplyTwoStrings(s1, s2):
    return str(int(s1) * int(s2))
