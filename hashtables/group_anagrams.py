class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for i in strs:
            j = "".join(sorted(i))
            if j in map:
                map[j].append(i)
            else:
                map[j] = [i]
        return list(map.values())