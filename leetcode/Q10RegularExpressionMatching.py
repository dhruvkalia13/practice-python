def isMatch(s: str, p: str) -> bool:
    map = {}
    def dp(i, j):
        if (i, j) not in map:
            if j == len(p):
                out = i == len(s)
            else:
                basic = i < len(s) and p[j] in {s[i], "."}
                if j + 1 < len(p) and p[j+1] == "*":
                    out = dp(i, j+2) or basic and dp(i+1, j)
                else:
                    out = basic and dp(i+1, j+1)
            map[i, j] = out
        return map[i, j]
    return dp(0, 0)


