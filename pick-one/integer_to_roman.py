class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        valuesDict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                      500: "D", 900: "CM", 1000: "M"}
        output = ""
        if num in values:
            return valuesDict.get(num)
        loc = 0
        while num != 0:
            for i in range(0, len(values) - 1):
                val = values[i]
                valNext = values[i + 1]
                if val <= num < valNext:
                    num = num - values[i]
                    output = output + valuesDict.get(values[i])
                    break
                elif num >= 1000:
                    num = num - 1000
                    output = output + valuesDict.get(1000)
                    break
        return output

