class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # use dfs
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        island = 0
        visited = set()

        def dfs(r, c):
            # base case
            if (r not in range(ROWS) or 
                c not in range(COLS) or 
                grid[r][c] != '1' or
                (r, c) in visited):
                return

            # at each level, mark itself as visited then visit its candidateds neighbors
            visited.add((r,c))
            dfs(r, c+1)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    # found a new island
                    island += 1
                    # find all islands connected to it
                    dfs(r, c)

        return island




