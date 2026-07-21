class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        curPath = []
        res = []
        self.helper(nums, 0, curPath, res)
        return res


    def helper(self, nums:List[int], level:int, curPath:List[int], res:List[Optional[List]]) -> None:
        # base case
        if level == len(nums):
            res.append(curPath[:])
            return

        # at each level, either choose it or not choose
        # 1. choose it, we can garuantee the current ele is not a duplicated ele 
        curPath.append(nums[level])
        self.helper(nums, level+1, curPath, res)
        curPath.pop()

        # 2. dont choose it, but remember to update level to the next unduplicated ele
        i = level + 1
        while i < len(nums) and nums[i] == nums[i-1]:
            i += 1
        self.helper(nums, i, curPath, res)

        