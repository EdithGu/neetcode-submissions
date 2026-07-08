class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = collections.deque() # (index, height) pair in non-decreasing order
        largestRectangle = 0

        for i, height in enumerate(heights):
            if not stack or stack[-1][1] <= height:
                stack.append((i, height))
                #print(f"stack: {stack}")
            else:

                while stack and stack[-1][1] > height:
                    #print(f"stack[-1][1] is : {stack[-1][1]} and current height is {height}")
                    largestRectangle = max(largestRectangle, stack[-1][1]*(i-stack[-1][0]))
                    #print(f"largestRectangle is {largestRectangle}")
                    stackedEleIndex = stack[-1][0]
                    stack.pop()

                stack.append((stackedEleIndex, height))

        #print(stack)
        # remember to post-processing

        while stack:
            i, height = stack[-1]
            rectangle_width = len(heights) - i 
            largestRectangle = max(largestRectangle, rectangle_width * height)
            stack.pop()
            #print(stack)


        return largestRectangle


        