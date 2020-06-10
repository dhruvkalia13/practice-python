def replaceElements(arr: [int]) -> [int]:
    # [17, 18, 5, 4, 6, 1]
    max_ele = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        temp = arr[i]
        arr[i] = max_ele
        max_ele = max(temp, max_ele)
    arr[len(arr) - 1] = -1
    return arr

print(replaceElements([17, 18, 5, 4, 6, 1]))