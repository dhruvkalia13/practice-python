class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        count, res = 0, 0
        # [1,0,1,1,0,1]
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            res = max(count, res)
        return res
