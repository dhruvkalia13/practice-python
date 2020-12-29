class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # cols = []
        # for i in range(len(matrix)):
        #     if 0 in matrix[i]:
        #         cols.append(matrix[i].index(0))
        #         matrix[i] = [0]*len(matrix[i])
        cols, rows = set(), set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        print(rows)
        print(cols)
        for i in rows:
            matrix[i] = [0] * len(matrix[i])
        for i in range(len(matrix)):
            for col in cols:
                matrix[i][col] = 0