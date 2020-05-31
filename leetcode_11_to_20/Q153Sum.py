def threeSum(nums: [int]) -> [[int]]:
    outList = []
    i = 0
    if len(nums) < 3:
        return []
    while i < len(nums):
        first = nums[i]
        j = 0
        while j < len(nums):
            if i == j:
                j += 1
                continue
            second = nums[j]
            third = 0 - (first + second)
            temp = nums.copy()
            if i > j:
                del temp[i]
                del temp[j]
            else:
                del temp[i]
                del temp[j-1]
            if third in temp:
                out = [first, second, third]
                out.sort()
                if out not in outList:
                    outList.append(out)
            j += 1
        i += 1
    return outList

# print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))
# print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([-1,0,1,0]))
print(threeSum([9,-9,4,12,12,0,-14,-7,10,-1,11,-10,-3,2,-9,0,8,-9,-5,-1,10,5,13,-5,-9,-12,9,-3,10,10,-10,4,8,1,-7,-2,-14,-6,6,11,8,-6,9,13,11,7,-10,-4,14,0,3,1,-10,-7,3,-12,-3,-11,0,-8,-15,5,3,8,13,11,13,-15,-9,4,3,6,5,-11,-4,-6,4,1,5,-5,-13,-7,11,-8,2,-1,-12,14,3,3,13,-5,-14,-7,11,14,-11,9,6,-13,-9,-13,1,11,-9,12,-10,2,-1,3,12,-7,3,0,0,12,6,3,3,-13,14,1,-3]))