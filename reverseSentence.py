# Reverse the order of words in a given string sentence. You can assume that sentence does not have any leading, trailing or repeating spaces.

# Example

# For sentence = "Man bites dog", the output should be
# reverseSentence(sentence) = "dog bites Man".

# Input/Output

# [time limit] 4000ms (py)
# [input] string sentence

# A string consisting of letters and spaces.

# Constraints:
# 1 ≤ sentence.length ≤ 2 · 104.

# [output] string


def reverseSentence(sentence):
#     parts = sentence.split()
#     sent2 = parts[0]
#     for part in parts[1:]:
#         sent2 = part + ' ' + sent2
        
#     return sent2
    parts = []
    word = ''
    for i in sentence:
        if i == ' ':
            if word:
                parts.append(word)
                word = ''
            parts.append(i)
            continue
        word += i
    parts.append(word)
    sent2 = ''
    for i in parts:
        sent2 = i + sent2
    return sent2
