class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        # first we found all the "o" on the boarder
        boarder_o = [(0, c) for c in range(COLS) if board[0][c]=="O"]
        boarder_o.extend((ROWS-1, c) for c in range(COLS) if board[ROWS-1][c]=="O")
        boarder_o.extend((r, 0) for r in range(1, ROWS-1) if board[r][0]=="O")
        boarder_o.extend((r, COLS-1) for r in range(1, ROWS-1) if board[r][COLS-1]=="O")

        visited = set()
        neis = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for r, c in boarder_o:
            self.dfs(r, c, board, visited, neis)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"


    def dfs(self, r, c, board, visited, neis):
        ROWS, COLS = len(board), len(board[0])

        # base case
        if (r not in range(ROWS) or
            c not in range(COLS) or
            (r, c) in visited or
            board[r][c] == 'X'
        ):
            return

        # at current level, we know (r,c) is a valid 'o' that connected to the boarder
        # mark it as visited and keep exploring its neighbors
        visited.add((r, c))
        board[r][c] = "#"
        for dr, dc in neis:
            row, col = r+dr, c+dc
            self.dfs(row, col, board, visited, neis)
