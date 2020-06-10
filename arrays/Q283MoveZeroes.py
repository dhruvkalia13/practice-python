def moveZeroes(nums: [int]):
    """
    Do not return anything, modify nums in-place instead.
    """
    # [0,1,0,3,12]
    start = 1
    i = 0
    while start < len(nums) and i < len(nums):
        if nums[i] == 0 and nums[start] != 0:
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start += 1
            i += 1
        elif nums[i] == 0 and nums[start] == 0:
            start += 1
        else:
            i += 1
            start += 1
    return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([2,1]))
print(moveZeroes([4,2,4,0,0,3,0,5,1,0]))