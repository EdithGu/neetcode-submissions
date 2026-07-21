class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        self.helper(n, 0, n, n, res, cur)
        return res

    def helper(self, n:int, level:int, left:int, right:int, res:List[str], cur:List[str]):
        # base case
        if level == n*2:
            res.append(''.join(cur))
            return

        # at each level, consider two states:
        # 1. add (
        if left > 0:
            cur.append('(')
            self.helper(n, level+1, left-1, right, res, cur)
            cur.pop()

        # 2. add )
        if right > left:
            cur.append(')')
            self.helper(n, level+1, left, right-1, res, cur)
            cur.pop()