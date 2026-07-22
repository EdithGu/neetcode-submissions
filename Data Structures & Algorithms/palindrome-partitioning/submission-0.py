class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        self.dfsHelper(s, 0, res, cur)
        return res

    def dfsHelper(self, s:str, level:int, res:List[List[str]], cur:List[str]) -> None:
        # base case
        if level == len(s):
            res.append(cur[:])
            return 

        # at each level, try to cut the word at every possible position
        for i in range(level+1, len(s)+1):
            # check whether s[level:i] is palindrome
            if not self.isPalindrome(s, level, i-1):
                continue
            cur.append(s[level:i])
            self.dfsHelper(s, i, res, cur)
            cur.pop()

    def isPalindrome(self, s:str, i:int, j:int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True
