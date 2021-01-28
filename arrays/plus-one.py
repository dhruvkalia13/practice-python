class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        if len(digits) == 1 and digits[0] == 9: return [1,0]
        if digits[-1] == 9:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9 or digits[i] == 10:
                    if i == 0:
                        digits[i] = 0
                        digits.insert(i,1)
                        return digits
                    else:
                        digits[i] = 0
                        digits[i-1] = digits[i-1] + 1
                else:
                    return digits
        digits[-1] = digits[-1] + 1
        return digits
print(Solution().plusOne([8,9,9,9]))