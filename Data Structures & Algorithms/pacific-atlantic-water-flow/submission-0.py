class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        pacific_boarders = set()
        atlantic_boarders = set()
        pacific_starting = []
        atlantic_starting = []
        for col in range(COLS):
            pacific_boarders.add((0, col))
            pacific_starting.append((0, col))
            atlantic_boarders.add((ROWS-1, col))
            atlantic_starting.append((ROWS-1, col))
        for row in range(ROWS):
            pacific_boarders.add((row, 0))
            pacific_starting.append((row, 0))
            atlantic_boarders.add((row, COLS-1))
            atlantic_starting.append((row, COLS-1))

        neis = ((0,1), (0,-1), (1,0), (-1,0))
        # find all nodes that can let water flow from it to pacific_boarders
        for r, c in pacific_starting:
            self.dfs(r, c, neis, pacific_boarders, heights)
        # find all nodes that can let water flow from it to atlantic_boarders
        for r, c in atlantic_starting:
            self.dfs(r, c, neis, atlantic_boarders, heights)

        return [[r,c] for r, c in (pacific_boarders & atlantic_boarders)]
            
    def dfs(self, r, c, neis, visited_valid:set, heights:List[List[int]]):    
        ROWS, COLS = len(heights), len(heights[0])
        for dr, dc in neis:
            row, col = r+dr, c+dc
            if (row in range(ROWS) and
                col in range(COLS) and
                (row, col) not in visited_valid and
                heights[row][col] >= heights[r][c]
            ):
                # (row, col) is a connected island
                visited_valid.add((row, col))
                self.dfs(row, col, neis, visited_valid, heights)
