def thirdMax(nums: [int]) -> int:
    nums.sort(reverse=True)
    i, count = 0, 0
    while i < len(nums):
        if count == 2:
            return nums[i]
        if i != len(nums)-1 and nums[i] != nums[i+1]:
            i += 1
            count += 1
        else:
            i += 1
    return nums[0]

print(thirdMax([2,2,3,1]))
print(thirdMax([1, 2]))
print(thirdMax([3, 2, 1]))
print(thirdMax([5,2,2]))
