class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        global_max = 0

        while left < right:
            cur = (right-left) * min(heights[left], heights[right])
            if cur > global_max:
                global_max = cur

            if heights[left] <= heights[right]:
                left += 1
            else: 
                right -= 1

        return global_max
        