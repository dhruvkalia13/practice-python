def reverse(self, x: int) -> int:
    s = str(x)
    if "-" not in s:
        out = int(s[::-1])
        if out <= -2 ** 31 or out >= 2 ** 31 - 1:
            return 0
        return out
    else:
        rev = s[::-1]
        rev = "-" + rev[:-1]
        out = int(rev)
        if out <= -2 ** 31 or out >= 2 ** 31 - 1:
            return 0
        return out