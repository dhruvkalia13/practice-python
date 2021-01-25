class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        biggest = max(nums)
        i = nums.index(biggest)
        nums.remove(biggest)
        big = max(nums)
        if biggest >= 2*big:
            return i
        return -1