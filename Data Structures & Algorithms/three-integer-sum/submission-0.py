class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array, so duplicate numbers will be together
        nums.sort()
        res = []
        i = 0
        # outer loop
        while i < len(nums)-2:
            remain = 0 - nums[i]
            # inner loop: 2 pointers
            l = i+1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == remain:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # keep update l and r until they point to a new ele
                    while(l < r and nums[l]==nums[l-1]):
                        l += 1 
                    while(l < r and nums[r]==nums[r+1]):
                        r -= 1
                elif nums[l] + nums[r] < remain:
                    l += 1
                    while(l < r and nums[l]==nums[l-1]):
                        l += 1 
                else:
                    r -= 1
                    while(l < r and nums[r]==nums[r+1]):
                        r -= 1
                
            # keep updating i to a new element
            i += 1
            while i < len(nums)-2 and nums[i] == nums[i-1]:
                i += 1

        return res







