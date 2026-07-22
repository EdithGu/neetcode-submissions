class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.dfs(n, 0, set(), set(), set(), [], res)
        return res
    
    def dfs(self, n:int, level:int, col_used:set, diag1_used:set, diag2_used:set, cur:List[str], res:List[List[str]]) -> None:
        # base case
        if level == n:
            res.append(cur[:])
            return

        # each level represents a row
        # at each level, try n columns
        for i in range(n):
            # check whether (level, i) is a valid place
            if i in col_used:
                continue
            if level-i in diag1_used:
                continue
            if level+i in diag2_used:
                continue

            # only place the queen when it's a valid place
            col_used.add(i)
            diag1_used.add(level-i)
            diag2_used.add(level+i)
            cur.append(i*"." + "Q" + (n-i-1)*".")
            
            self.dfs(n, level+1, col_used, diag1_used, diag2_used, cur, res)
            
            cur.pop()
            col_used.remove(i)
            diag1_used.remove(level-i)
            diag2_used.remove(level+i)




            
            