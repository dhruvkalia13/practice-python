class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = []
        for i, val in enumerate(s):
            if val == c:
                pos.append(i)
        print(pos)
        out = []
        for i, val in enumerate(s):
            if val == c:
                out.append(0)
            else:
                out.append(min([abs(p - i) for p in pos]))
        return out