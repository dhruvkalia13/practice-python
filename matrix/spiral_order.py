class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        count = 0
        output = []
        curr = "R"
        i, j = 0, 0
        nrow = len(matrix) - 1
        ncol = len(matrix[0]) - 1
        nrow_min, ncol_min = 1, 0
        while count != (len(matrix)) * (len(matrix[0])):
            output.append(matrix[i][j])
            if j == ncol and curr == "R":
                curr = "D"
                ncol -= 1
            if i == nrow and curr == "D":
                curr = "L"
                nrow -= 1
            if i == nrow_min and curr == "U":
                curr = "R"
                nrow_min += 1
            if j == ncol_min and curr == "L":
                curr = "U"
                ncol_min += 1

            if curr == "R":
                j += 1
            elif curr == "D":
                i += 1
            elif curr == "L":
                j -= 1
            elif curr == "U":
                i -= 1
            count += 1

        return output