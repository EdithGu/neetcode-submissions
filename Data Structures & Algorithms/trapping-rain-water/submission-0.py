class Solution:
    def trap(self, height: List[int]) -> int:
        # space complexity O(1) version
        trapped_water = 0

        left = 0
        right = len(height)-1
        left_max = 0
        right_max = 0
        while left <= right:
            # the amount of water each position can hold only depends on the smaller max
            while left <= right and left_max <= right_max:
                cur_water = max(left_max - height[left], 0)
                trapped_water += cur_water
                left_max = max(left_max, height[left])
                left += 1
            while left <= right and left_max > right_max:
                cur_water =  max(right_max - height[right], 0)     
                trapped_water += cur_water
                right_max = max(right_max, height[right])
                right -= 1

        return trapped_water
            
        