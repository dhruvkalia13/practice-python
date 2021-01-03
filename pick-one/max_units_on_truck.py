class Solution:
    def maximumUnits(self, boxTypes: [[int]], truckSize: int) -> int:
        a = {}
        for boxType in boxTypes:
            if boxType[1] in a.keys():
                a[boxType[1]] += boxType[0]
            else:
                a[boxType[1]] = boxType[0]

        number_of_units = a.keys()
        number_of_units = sorted(number_of_units, reverse=True)
        output = 0
        for units_each in number_of_units:
            boxes = a[units_each]
            if truckSize == 0:
                return output
            if truckSize <= boxes:
                output += truckSize * units_each
                return output
            if truckSize > boxes:
                truckSize -= boxes
                output += units_each * boxes
                continue
        return output


print(Solution().maximumUnits([[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]] ,13))
print(Solution().maximumUnits([[1,3],[2,2],[3,1]],4))
print(Solution().maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
