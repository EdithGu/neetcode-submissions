class Solution:
    digits_map = {2:"abc", 3:"def", 4:"ghi", 5:"jkl",6:"mno",7:"pqrs", 8:"tuv", 9:"wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        cur = []
        res = []
        self.dfs(digits, 0, cur, res)
        return res

    def dfs(self, digits, level, cur:List[str], res:List) -> None:
        # base case
        if level == len(digits):
            res.append(''.join(cur))
            return

        # each level represent a digit at its corrosponding position
        # at each level, try all of its mapping characters
        for char in self.digits_map[int(digits[level])]:
            cur.append(char)
            self.dfs(digits, level+1, cur, res)
            cur.pop()


    