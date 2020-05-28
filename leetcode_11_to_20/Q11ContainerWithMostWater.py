def maxArea1(height: []) -> int:
    l = height
    max_area = 0
    i = 0
    j = len(l) - 1
    while i < j:
        start = l[i]
        end = l[j]
        max_area = max(max_area, (min(start, end) * (j - i)))
        if start > end:
            j -= 1
        else:
            i += 1
    return max_area

print(maxArea1([1,1]))