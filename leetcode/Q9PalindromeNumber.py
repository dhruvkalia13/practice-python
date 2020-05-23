def isPalindrome(self, x: int) -> bool:
    s = str(x)
    rev = s[::-1]
    if rev == s:
        return True
    else:
        return False