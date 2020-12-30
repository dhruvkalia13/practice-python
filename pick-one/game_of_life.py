class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        old = [[0] * len(board[0])] * len(board)
        for i, row in enumerate(board):
            old[i] = row.copy()
        for i in range(len(old)):
            for j in range(len(old[i])):
                val = []
                if 0 <= i - 1 <= len(old) - 1 and 0 <= j - 1 <= len(old[i]) - 1:
                    val.append(old[i - 1][j - 1])
                if 0 <= i - 1 <= len(old) - 1 and 0 <= j <= len(old[i]) - 1:
                    val.append(old[i - 1][j])
                if 0 <= i - 1 <= len(old) - 1 and 0 <= j + 1 <= len(old[i]) - 1:
                    val.append(old[i - 1][j + 1])
                if 0 <= i <= len(old) - 1 and 0 <= j - 1 <= len(old[i]) - 1:
                    val.append(old[i][j - 1])
                if 0 <= i <= len(old) - 1 and 0 <= j + 1 <= len(old[i]) - 1:
                    val.append(old[i][j + 1])
                if 0 <= i + 1 <= len(old) - 1 and 0 <= j - 1 <= len(old[i]) - 1:
                    val.append(old[i + 1][j - 1])
                if 0 <= i + 1 <= len(old) - 1 and 0 <= j <= len(old[i]) - 1:
                    val.append(old[i + 1][j])
                if 0 <= i + 1 <= len(old) - 1 and 0 <= j + 1 <= len(old[i]) - 1:
                    val.append(old[i + 1][j + 1])

                if old[i][j] == 1 and val.count(1) < 2:
                    board[i][j] = 0
                elif old[i][j] == 1 and 3 >= val.count(1) >= 2:
                    board[i][j] = 1
                elif old[i][j] == 1 and val.count(1) > 3:
                    board[i][j] = 0
                elif old[i][j] == 0 and val.count(1) == 3:
                    board[i][j] = 1
        return board

print(Solution.gameOfLife(Solution(),[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))