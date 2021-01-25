class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        a = 0
        for i, val in enumerate(nums):
            if 2 * a + val == s:
                return i
            a += val

        return -1