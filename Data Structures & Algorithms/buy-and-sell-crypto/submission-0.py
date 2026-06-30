class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        globalMax = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            curProfit = prices[right] - prices[left]
            #print(f"left and right: {left} and {right}, curProfit: {curProfit}")
            globalMax = max(curProfit, globalMax)
            #print(f"gobalMax: {globalMax} \n")

        return globalMax
