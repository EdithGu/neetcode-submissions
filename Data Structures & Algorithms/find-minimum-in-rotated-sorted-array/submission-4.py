class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right-1:
            mid = left + (right-left)//2

            if nums[mid] < nums[0]:
                right = mid
            elif nums[mid] > nums[0]:
                left = mid + 1


        # post checking
        if nums[left] < nums[0]:
            return nums[left]
        elif nums[right] < nums[0]:
            return nums[right]
        else:
            return nums[0]