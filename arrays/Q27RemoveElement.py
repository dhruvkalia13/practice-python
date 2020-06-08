def removeElement(nums: [int], val: int) -> int:
    last = len(nums) - 1
    l = [item for item in nums if item == val]
    occ = len(l)

    def swap(arr: [int], pos1: int, pos2: int):
        temp = arr[pos1]
        arr[pos1] = arr[pos2]
        arr[pos2] = temp

    i = 0
    while i < len(nums) - occ:
        if nums[i] == val and nums[last] != val:
            swap(nums, i, last)
            last -= 1
            i += 1
        elif nums[last] == val:
            last -= 1
        else:
            i += 1
    print(nums[0:len(nums) - occ])
    return len(nums) - occ

# print(removeElement([0,1,2,2,3,0,4,2], 2))
print(removeElement([3,2,2,3], 3))