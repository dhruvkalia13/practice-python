class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for i, val in enumerate(s):
            if val in map:
                map[val] += 1
            else:
                map[val] = 1
        for i, val in enumerate(s):
            if map[val] == 1:
                return i
        return -1