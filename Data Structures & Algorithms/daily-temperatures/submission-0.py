class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = collections.deque() # index of temperature
        res = [0] * len(temperatures)
        
        for i, temperature in enumerate(temperatures):
                
            while stack and temperatures[stack[-1]] < temperature:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)

        return res


# temperatures = [30,38,30,36,35,40,28]
#                                      i=6
# stack = [5, 6  ]
# res = [1 4 1 2 1 0 0]
