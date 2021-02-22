class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s, map_t = {}, {}
        for i in range(len(s)):
            if s[i] in map_s:
                map_s[s[i]].append(i)
            else:
                map_s[s[i]] = [i]
            if t[i] in map_t:
                map_t[t[i]].append(i)
            else:
                map_t[t[i]] = [i]
        return list(map_s.values()) == list(map_t.values())