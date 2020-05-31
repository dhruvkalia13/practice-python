def longestCommonPrefix(strs: [str]) -> str:
    if len(strs) > 0:
        firstItem = strs[0]
    else:
        return ""
    out = ""
    for i in range(1, len(firstItem)+1):
        temp = ""
        fail = False
        for s in strs:
            if strs.index(s) == 0:
                temp = s[:i]
                continue
            if s[:i] == firstItem[:i]:
                temp = s[:i]
                continue
            else:
                fail = True
                break
        out = temp if fail is False else out
    return out

print(longestCommonPrefix(["a"]))