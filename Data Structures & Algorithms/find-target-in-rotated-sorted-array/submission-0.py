class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < right-1:
            mid = left + (right-left)//2

            # check which part is sorted array
            if nums[mid] > nums[0]:
                # left part is sorted array
                
                # check if target in sorted array
                if target >= nums[left] and target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                # right part is sorted array

                # check if target in sorted array
                if target >= nums[mid] and target <= nums[right]:
                    left = mid
                else:
                    right = mid-1

        # post checking
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1