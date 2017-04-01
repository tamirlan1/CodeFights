# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully justified on both the left and the right. Words should be packed in a greedy approach; that is, pack as many words as possible in each line. Add extra spaces when necessary so that each line has exactly L characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right. For the last line of text and lines with one word only, the words should be left justified with no extra space inserted between them.

# Example

# For
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# and L = 16, the output should be

# textJustification(words, L) = ["This    is    an",
#                                "example  of text",
#                                "justification.  "]
# Input/Output

# [time limit] 4000ms (py)
# [input] array.string words

# An array of words. Each word is guaranteed not to exceed L in length.

# Constraints:
# 1 ≤ words.length ≤ 150,
# 0 ≤ words[i].length ≤ L.

# [input] integer L

# The length that all the lines in the output array should be.

# Constraints:
# 1 ≤ L ≤ 60.

# [output] array.string

# The formatted text as an array containing lines of text, with each line having a length of L.

def textJustification(words, L):
    lines = []
    elements = []
    spaces = []
    # line = ''
    len_elems = 0
    for w in words:
        # print w
        if len_elems + len(elements) + len(w) <= L:
            # print 1
            elements.append(w)
            len_elems += len(w)
        else:
            # print 2
            line = create_line(elements, len_elems, L)
            
            lines.append(line)
            elements = [w]
            spaces = []
            # line = ''
            len_elems = len(w)
    else:
        if elements:
            line = create_line(elements, len_elems, L, spec=1)
            lines.append(line)
    return lines

def create_line(elements, len_elems, L, spec=0):
    # print elements, len_elems
    line = ''
    spaces = (len(elements) - 1)*[' ']
    if len(spaces) == 0:
        if L == len_elems:
    		line = elements[0]
    		return line
        spaces = [' ']
    if spec == 1:
        for i in range(len(spaces)):
            line += elements[i] + spaces[i]
        if len(elements) > 1:
            line += elements[i+1]
        diff = L - len(line)
        # print diff
        if diff > 0:
            line += ' '*diff
        return line

    else:
        extra_spaces = L - len(spaces) - len_elems
        while extra_spaces > 0:
            for i in range(len(spaces)):
                spaces[i] += ' '
                extra_spaces -= 1
                if extra_spaces == 0:
                    break
        for i in range(len(spaces)):
            line += elements[i] + spaces[i]
        if len(elements) > 1:
            line += elements[i+1]
        return line