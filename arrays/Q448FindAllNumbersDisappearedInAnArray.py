def findDisappearedNumbers(nums: [int]) -> [int]:
    for i, n in enumerate(nums):
        if n > 0:
            while n > 0:
                tmp = nums[n - 1]
                nums[n - 1] = -1
                n = tmp
    res = []
    for i in range(len(nums)):
        if nums[i] >= 0:
            res.append(i + 1)
    return res

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
# print(findDisappearedNumbers([1,1]))