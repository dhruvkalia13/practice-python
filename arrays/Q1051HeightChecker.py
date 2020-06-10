def heightChecker(heights: [int]) -> int:
    s, count = sorted(heights), 0
    for i in range(len(heights)):
        if heights[i] != s[i]:
            count += 1
    print(s)
    return count

print(heightChecker([5,1,2,3,4]))