def isThisPalindrome(s):
    rev = s[::-1]
    return True if rev == s else False


def longestPalindrome(s: str) -> str:
    # method to check if a string is palindrome, this will be called for each substring in this string
    # if it is palindrome, then store this substring and its length in dict
    if isThisPalindrome(s):
        return s
    length = len(s)
    for i in range(0, length):
        end = length - (i + 1)
        start = 0
        for j in range(-2, i):
            temp = s[start: end]
            if isThisPalindrome(temp):
                return temp
            start += 1
            end += 1


print(longestPalindrome("cbbd"))
