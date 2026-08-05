class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # BFS searching range: [max((0,0), (n-1,n-1)), max_value]
        max_value = float('-inf')
        rows_num = len(grid)
        cols_num = len(grid[0])
        for r in range(rows_num):
            for c in range(cols_num):
                max_value = max(max_value, grid[r][c])

        i = max(grid[0][0], grid[rows_num-1][cols_num-1])
        j = max_value

        while i < j:
            # at each searching step
            t = i + (j-i)//2
            # dfs((0,0))
            visited = set()
            flag = [False]
            self.canReach(0, 0, t, grid, visited, flag)

            if flag[0] == True:
                # if can reach with time t, t might be the solution, but the ele at t's right side cannot be the solution
                j = t
            else:
                # if cannot reach with time t, t is too small, 
                # t cannot be the solution, and the eles at t's left side cannot be solution either
                i = t+1

        return i

        
    def canReach(self, r:int, c:int, time:int, grid:List[List[int]], visited:set(), flag:[bool]) -> None:      
        # at each dfs level:
            # check validy:
                # out of range / if already visited / value strictly greater than t
        if (r not in range(len(grid)) or
            c not in range(len(grid[0])) or
            (r, c) in visited or
            flag[0] == True or
            grid[r][c] > time
        ):
            return
        
        # if a valid point:
        # mark it as visited
        visited.add((r,c))
        # check if we reach to the destination
        if r == len(grid)-1 and c == len(grid[0])-1:
            flag[0] = True
            return
        neis = [(0,1),(0,-1),(1,0), (-1,0)]
        for dr, dc in neis:
            self.canReach(r+dr, c+dc, time, grid, visited, flag)
            # explore its 4 neighbors
            









