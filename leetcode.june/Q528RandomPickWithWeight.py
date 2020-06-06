import bisect
import random


class Solution:
    cumSum = []

    def __init__(self, w: [int]):
        # w = w[0]
        self.cumSum = [w[0]]
        for i in range(1, len(w)):
            self.cumSum.append(self.cumSum[i - 1] + w[i])
        print("Cumsum is " + str(self.cumSum))

    def pickIndex(self) -> int:
        x = random.randint(1, self.cumSum[-1])
        return bisect.bisect_left(self.cumSum, x)

# Your Solution object will be instantiated and called as such:
# obj = Solution([3,14,1,7])
# param_1 = obj.pickIndex()
# print(param_1)

# abs_diff_func = lambda val: abs(val - rand)
# res = min(self.cumSum, key=abs_diff_func)
