class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    # found a new land
                    curArea = [0]
                    self.dfs(grid, r, c, curArea, visited)
                    maxArea = max(maxArea, curArea[0])

        return maxArea



    def dfs(self, grid:List[List], r:int, c:int, curArea:List, visited:set):
        ROWS, COLS = len(grid), len(grid[0])

        # base case: check the validy of a cell
        if (
            r not in range(ROWS) or
            c not in range(COLS) or
            grid[r][c] != 1 or
            (r,c) in visited
        ):
            return


        # at each level, plus the area by one and check its four neighbors
        curArea[0] += 1
        visited.add((r,c))
        self.dfs(grid, r+1, c, curArea, visited)
        self.dfs(grid, r-1, c, curArea, visited)
        self.dfs(grid, r, c+1, curArea, visited)
        self.dfs(grid, r, c-1, curArea, visited)

