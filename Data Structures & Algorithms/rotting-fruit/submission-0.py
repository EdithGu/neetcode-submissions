class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = collections.deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    queue.append((row, col))

        time = 0
        while queue:
            # record how many elements needs to be processed at the current level
            level_size = len(queue)

            for i in range(level_size):
                row, col = queue.popleft()
                neis = ((0,1), (0,-1), (1,0), (-1,0))
                for dr, dc in neis:
                    r, c = row+dr, col+dc
                    if (
                        r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == 1
                    ):
                        grid[r][c] = 2
                        queue.append((r,c))

            if queue:
                # only update time when there is fresh fruit affected
                time += 1

        # post-checking
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1

        return time
