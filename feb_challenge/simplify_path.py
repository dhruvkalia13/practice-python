class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        fresh = []
        for item in arr:
            if not item or item == ".":
                continue
            if item == "..":
                if fresh:
                    fresh.pop()
            else:
                fresh.append(item)
        out = ''
        for item in fresh:
            out += '/'
            out += item
        if out:
            return out
        return '/'