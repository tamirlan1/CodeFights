# Given a string of digits, return all of the possible letter combinations that the number could represent. The mapping of digits to letters is the same as you would find on a telephone's buttons, as in the example below:



# The resulting array should be sorted lexicographically.

# Example

# For buttons = "42", the output should be
# pressingButtons(buttons) = ["ga", "gb", "gc", "ha", "hb", "hc", "ia", "ib", "ic"].

# Input/Output

# [time limit] 4000ms (py)
# [input] string buttons

# A string composed of digits ranging from '2' to '9'.

# Guaranteed constraints:

# 0 ≤ buttons.length ≤ 7.

# [output] array.string


def pressingButtons(buttons):
    lookup = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
              '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    all_combins = []
    for i in buttons:
        if not all_combins:
            for letter in lookup[i]:
                all_combins.append(letter)
        else:
            all_combins2 = []
            for letter in lookup[i]:
                for word in all_combins:
                    all_combins2.append(word + letter)
            all_combins = all_combins2
    return sorted(all_combins)
    # output = []
    # for let in all_combins:
    #     for i in let:
            
