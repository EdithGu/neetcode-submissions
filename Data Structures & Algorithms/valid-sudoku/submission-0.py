class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check by rows
        print(0%3)
        for row in range(0, len(board)):
            numberSet = set()
            for col in range(0, len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in numberSet:
                    print(f"False on board{row}{col} in row check")
                    return False
                else:
                    numberSet.add(board[row][col])

        # check by cols
        for col in range(0, len(board[0])):
            numberSet = set()
            for row in range(0, len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in numberSet:
                    print(f"False on board{row}{col} in col check")
                    return False
                else:
                    numberSet.add(board[row][col])

        # check by 3*3 grid
        for row_index in range(0,3):
            for col_index in range(0,3):
                numberSet = set()
                for i in range(9):
                    row = i // 3 + row_index * 3
                    col = i % 3 + col_index * 3
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in numberSet:
                        print(f"False on board{row}{col} in grid check")
                        return False
                    else:
                        numberSet.add(board[row][col])

        return True


        