class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right-left)//2

            if self.canFinish(mid, piles, h):
                right = mid
            else:
                left = mid+1

        if self.canFinish(left, piles, h):
            return left
        else:
            return -1

    def canFinish(self, rate:int, piles:List[int], h:int) -> bool:
        time = 0
        for pile in piles:
            curTime = math.ceil(pile / rate)
            time += curTime
        
        return time <= h