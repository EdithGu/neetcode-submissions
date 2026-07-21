class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        self.helper(nums, 0, cur, res, target)
        return res

    def helper(self, nums:List[int], level:int, cur:List, res:List[Optional[List]], remaining:int) -> None:
        # base case
        if remaining == 0:
            res.append(cur[:])
            return
        if level == len(nums):
            return

        # at each level, we can try adding cur element 0 - remaining//ele_val times
        for i in range(remaining // nums[level] + 1):
            cur.extend([nums[level] for _ in range(i)])
            self.helper(nums, level+1, cur, res, remaining-nums[level]*i)
            for _ in range(i):
                cur.pop()