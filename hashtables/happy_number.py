class Solution:
    def isHappy(self, n: int) -> bool:
        out = set()
        while n != 1:
            arr = [int(i) for i in str(n)]
            n = sum([a ** 2 for a in arr])
            if n in out:
                return False
            else:
                out.add(n)
        print(out)
        return True
