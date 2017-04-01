# You have two strings, s and t. The string t contains only unique elements. Find and return the minimum consecutive substring of s that contains all of the elements from t.

# It's guaranteed that the answer exists. If there are several answers, return the one which starts from the smallest index.

# Example

# For s = "adobecodebanc" and t = "abc", the output should be
# minSubstringWithAllChars(s, t) = "banc".

# Input/Output

# [time limit] 4000ms (py)
# [input] string s

# A string consisting only of lowercase English letters.

# Guaranteed constraints:
# 0 ≤ s.length ≤ 100.

# [input] string t

# A string consisting only of unique lowercase English letters.

# Guaranteed constraints:
# 0 ≤ t.length ≤ min(26, s.length).

# [output] string

def minSubstringWithAllChars(s, t):
    if len(t) == 1:
        return t
    combins = []
    elems_t = list(t)
    len_cand = 1000000
    candidate = ''
    for i in range(len(s)):
        letter = s[i]
        if letter not in elems_t:
            continue
        t1 = list(t)
        t1.remove(letter)
        substring = s[i+1:]
        try:    
            max_index = max([substring.index(j) for j in t1])
        except:
            continue
        new_candidate = s[i:i+max_index+2]
        if len(new_candidate) < len_cand:
            len_cand = len(new_candidate)
            candidate = new_candidate
        # print combins

    return candidate