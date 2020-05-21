def twoSum(nums, target):
    map = {nums[i]: i for i in range(0, len(nums))}
    for i in range(0, len(nums)):
        comp = target - nums[i]
        if comp in map and map[comp] != i:
            return [map[comp], i]


print(twoSum([2, 7, 11, 15], 9))
