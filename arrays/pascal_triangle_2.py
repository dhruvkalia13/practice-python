class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i = 2
        output = [[1],[1,1]]
        while i <= rowIndex:
            curr = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(output[i-1][j-1] + output[i-1][j])
            # print(curr)
            output.append(curr)
            i += 1
        return output[rowIndex]