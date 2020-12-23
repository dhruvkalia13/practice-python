def reverseString(s: [str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """

    def helper(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

    helper(0, len(s) - 1)
    return s
print(reverseString(["a","b","c"]))