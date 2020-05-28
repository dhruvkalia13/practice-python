# Symbol       Value
# I     4        1
# V     1       5
# X             10
# L             50
# C             100
# D             500
# M             1000
def intToRoman(s: str) -> int:
    out = 0
    # val = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    symbols = ["I", "IV", "V", " IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    map = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
    results = []
    i = 0
    while i != len(s):
        c = s[i]
        if i != len(s)-1 and c in ["I", "X", "C"] and s[i+1] in ["V", "X", "L", "C", "D", "M"]:
            check = c + s[i+1]
            if check in map:
                val = map[check]
                i += 2
                out = out + val
                continue

        val = map[c]
        out = out + val
        i += 1
    return out


print(intToRoman("LVIII"))
