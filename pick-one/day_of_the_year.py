class Solution:

    def dayOfYear(self, date: str) -> int:
        a = date.split("-", 3)
        year = int(a[0])
        month = int(a[1])
        date = int(a[2])
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days[2] = 29
        output = 0
        for i in range(1, month + 1):
            if i == month:
                output += date
                return output
            output += days[i]
        return output

print(Solution.dayOfYear(Solution(),"2019-02-10"))

