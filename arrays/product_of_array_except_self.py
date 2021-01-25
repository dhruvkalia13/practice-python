class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        l = 1
        for i, val in enumerate(nums):
            left.append(l)
            l = l * val
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            a = left[i]
            left[i] = a * r
            r = r * nums[i]
        return left
