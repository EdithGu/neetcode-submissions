class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        self.helper(nums, 0, res, cur)
        return res

    def helper(self, nums:List[int], level:int, res:List[Optional[List]], cur:List[int]) -> None:
        # base case
        if level == len(nums):
            res.append(cur[:])
            return

        # at current level: only 2 operations, either choose it or not
        # 1. choose it
        cur.append(nums[level])
        self.helper(nums, level+1, res, cur)
        cur.pop()

        # 2. not choose it
        self.helper(nums, level+1, res, cur)
