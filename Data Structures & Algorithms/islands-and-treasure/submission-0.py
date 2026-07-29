class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        step = 1
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                r, c = queue.popleft()
                nei = ((0,1), (0,-1), (1,0), (-1,0))
                for dr, dc in nei:
                    row, col = r+dr, c+dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 2147483647:
                        grid[row][col] = step
                        queue.append((row, col))

            step += 1

