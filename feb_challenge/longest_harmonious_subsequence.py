class Solution:
    def findLHS(self, nums: List[int]) -> int:
        map = {}
        for i, val in enumerate(nums):
            if val in map:
                map[val] += 1
            else:
                map[val] = 1
        out = 0
        # print(map)
        for key, value in map.items():
            if key + 1 in map:
                out = max(out, map[key] + map[key + 1])
        return out

