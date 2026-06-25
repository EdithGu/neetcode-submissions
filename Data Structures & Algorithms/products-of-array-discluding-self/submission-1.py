class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(1) space complexity version
        res = [0] * len(nums)
        res[0] = 1 

        # first pass through from head to tail
        # value at i is the cumulative product from head to i-1
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1] 

        print(res)
        # second pass through from tail to head
        postfix_product = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *=  postfix_product
            postfix_product *= nums[i]

        return res 




        