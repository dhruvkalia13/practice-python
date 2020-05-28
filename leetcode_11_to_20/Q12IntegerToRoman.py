# Symbol       Value
# I     4        1
# V     1       5
# X             10
# L             50
# C             100
# D             500
# M             1000
def intToRoman(num: int) -> str:
    # 12
    out = ""
    val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    map = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    results = []
    while num != 0:
        i = 12
        while i >= 0:
            if val[i] <= num:
                sym = map[val[i]]
                results.append(sym)
                break
            i -= 1
        num = num - val[i]
    # rev = results[::-1]
    out = "".join(results)
    return out


print(intToRoman(58))
