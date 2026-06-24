class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product and postfix product
        prefix = [nums[0] for _ in range(len(nums))]
        postfix = [nums[-1] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            postfix[len(nums)-i-1] = postfix[len(nums)-i] * nums[len(nums)-i-1]

        res = [0 for _ in range(len(nums))]
        res[0] = postfix[1]
        res[-1] = prefix[-2] 
        for i in range(1, len(nums)-1):
            res[i] = prefix[i-1] * postfix[i+1]

        return res


        