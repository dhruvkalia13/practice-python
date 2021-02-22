class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {val : i for i, val in enumerate(nums)}
        for i, val in enumerate(nums):
            if target-val in map and map[target-val] != i:
                return [i, map[target-val]]
        return []