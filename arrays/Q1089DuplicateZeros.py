def duplicateZeros(arr: [int]):
    """
    Do not return anything, modify arr in-place instead.
    """
    """First we need to find how many zeroes are there to be duplicated"""
    # [1,0,2,3,0,4,5,0]
    length_ = len(arr) - 1
    dups = 0
    for left in range(0, length_ +1):
        if left > length_ - dups:
            break
        if arr[left] == 0 and left == length_ - dups:
            arr[length_] = 0
            length_ -= 1
            break
        if arr[left] == 0:
            dups += 1

    last = length_ - dups
    for i in range(last, -1, -1):
        if arr[i] == 0:
            arr[i + dups] = 0
            dups -= 1
            arr[i + dups] = 0
        else:
            arr[i + dups] = arr[i]
    return arr

print(duplicateZeros([1,0,2,3,0,4,5,0]))