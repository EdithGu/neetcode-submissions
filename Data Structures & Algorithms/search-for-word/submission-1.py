class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                isMatch = self.dfs(board, word, r, c, 0, set())
                if isMatch:
                    return True

        return False

    def dfs(self, board:List[List[str]], word:str, r:int, c:int, level:int, visited:set) -> bool:
        ROWS, COLS = len(board), len(board[0])
        if level == len(word):
            return True
        if (
            min(r, c) < 0 
            or r >= ROWS or c >= COLS or 
            (r, c) in visited 
            or board[r][c] != word[level]
        ):
            return False


        # at each level, consider its 4 adjascent cells
        
        visited.add((r,c))
        isMatch = (
            self.dfs(board, word, r+1, c, level+1, visited)
            or self.dfs(board, word, r-1, c, level+1, visited)
            or self.dfs(board, word, r, c+1, level+1, visited)
            or self.dfs(board, word, r, c-1, level+1, visited)
        )
        visited.remove((r,c))

        return isMatch
