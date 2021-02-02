class Solution:
    def fib(self, n: int) -> int:
        cache = {}

        def getN(n):
            if n in cache:
                return cache[n]
            if n == 0:
                cache[n] = 0
                return 0
            elif n == 1:
                cache[n] = 1
                return 1
            else:
                cache[n] = getN(n - 1) + getN(n - 2)
                return cache[n]

        return getN(n)
