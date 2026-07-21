class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        cur = []
        self.helper(candidates, target, 0, res, cur)
        return res

    def helper(self, candidates:List[int], remaining:int, level:int, res:List[List], cur:List[int] ) -> None:
        # collection case
        if remaining == 0:
            res.append(cur[:])
            return

        # base case
        if level == len(candidates):
            return

        # at each level, there are 2 states: choose or not choose
        # 1. choose it if valid
        if candidates[level] <= remaining:
            cur.append(candidates[level])
            self.helper(candidates, remaining-candidates[level], level+1, res, cur)
            cur.pop()
        else:
            return

        # 2. not choose it, but also skip all the following same value, jump directly to the next distinct value
        i = level+1
        while i < len(candidates) and candidates[i] == candidates[i-1]:
            i += 1
        self.helper(candidates, remaining, i, res, cur)
