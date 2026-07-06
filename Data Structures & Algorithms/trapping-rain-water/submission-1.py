class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        left = 0 
        right = len(height)-1
        total = 0
        while left <= right:
            if leftmax <= rightmax:
                leftmax = max(leftmax, height[left])
                cur_water = max(min(leftmax, rightmax) - height[left], 0)
                total += cur_water
                left += 1
            else:
                rightmax = max(rightmax, height[right])
                cur_water = max(min(leftmax, rightmax) - height[right], 0)
                total += cur_water
                right -= 1
            
        return total
