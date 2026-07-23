class Solution:
    class stonesMaxHeapItem:
        def __init__(self, weight:int):
            self.weight = weight

        def __lt__(self, other):
            return self.weight >= other.weight

    def lastStoneWeight(self, stones: List[int]) -> int:
        array = [self.stonesMaxHeapItem(i) for i in stones]
        heapq.heapify(array)
        while len(array)>=2:
            moreHeavy = heapq.heappop(array)
            lessHeavy = heapq.heappop(array)
            if moreHeavy.weight > lessHeavy.weight:
                heapq.heappush(array, self.stonesMaxHeapItem(moreHeavy.weight-lessHeavy.weight))

        if len(array) == 1:
            return array[0].weight
        else:
            return 0
