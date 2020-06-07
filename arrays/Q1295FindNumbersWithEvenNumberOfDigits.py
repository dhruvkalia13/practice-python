class Solution:
    def findNumbers(self, nums: [int]) -> int:
        return len(list(filter(lambda n : len(str(n)) % 2 == 0, nums)))