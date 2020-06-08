def removeDuplicates(nums: [int]):
    start, count = 0, 0
    for i in range(1, len(nums)):
        if nums[start] == nums[i]:
            i += 1
        else:
            start += 1
            nums[start] = nums[i]
    return start+1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))