class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, res)
        return res

    def helper(self, nums:List[int], level:int, res:List[List[int]]) -> None:
        # base case
        if level == len(nums):
            res.append(nums[:])
            return

        # at each level, consider n-level states, put each candidate value to level position
        for i in range(level, len(nums)):
            self.swap(nums, i, level)
            self.helper(nums, level+1, res)
            self.swap(nums, i, level)


    def swap(self, nums:List[int], i:int, j:int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp