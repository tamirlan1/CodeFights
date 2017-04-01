# Convert a non-negative integer to its equivalent representation as words in English.

# Example

# For num = 1, the output should be
# integerToEnglishWords(num) = "One";
# For num = 123, the output should be
# integerToEnglishWords(num) = "One Hundred Twenty Three";
# For num = 12345, the output should be
# integerToEnglishWords(num) = "Twelve Thousand Three Hundred Forty Five";
# For num = 1234567, the output should be
# integerToEnglishWords(num) = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven".
# Input/Output

# [time limit] 4000ms (py)
# [input] integer num

# Guaranteed constraints:

# 0 ≤ num ≤ 231 - 1.

# [output] string


def integerToEnglishWords(num):
    lookup = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
            20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
            70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
    
    if num/10 == 0:
        return lookup[num]
    elif num/100 == 0:
        x = 10
        if num in lookup.keys():
            return lookup[num]
        else:
            # ans = integerToEnglishWords(num%x)
            # if ans == 0:
            #     return lookup[num/x*x]
            # else:
            return lookup[num/x*x] + ' ' + integerToEnglishWords(num%x)
    elif num/1000 == 0:
        x = 100
        ans = integerToEnglishWords(num%x)
        if ans == 'Zero':
            return integerToEnglishWords(num/x) + ' Hundred'
        else:
            return integerToEnglishWords(num/x) + ' Hundred ' + ans

    elif num/1000000 == 0:
        x = 1000
        ans = integerToEnglishWords(num%x)
        if ans == 'Zero':
            return integerToEnglishWords(num/x) + ' Thousand'
        else:
            return integerToEnglishWords(num/x) + ' Thousand ' + ans

    elif num/1000000000 == 0:
        x = 1000000
        ans = integerToEnglishWords(num%x)
        if ans == 'Zero':
            return integerToEnglishWords(num/x) + ' Million'
        else:
            return integerToEnglishWords(num/x) + ' Million ' + ans

    else:
        x = 1000000000
        ans = integerToEnglishWords(num%x)
        if ans == 'Zero':
            return integerToEnglishWords(num/x) + ' Billion'
        else:
            return integerToEnglishWords(num/x) + ' Billion ' + ans