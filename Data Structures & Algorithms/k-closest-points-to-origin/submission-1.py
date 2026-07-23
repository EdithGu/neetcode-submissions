class Solution:
    class maxHeapItemPoints:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __lt__(self, other):
            if self.x ** 2 + self.y ** 2 > other.x ** 2 + other.y ** 2:
                return True
            else:
                return False

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [self.maxHeapItemPoints(i[0], i[1]) for i in points]
        heap = []
        for i in points:
            heapq.heappush(heap, i)
            if len(heap) > k:
                heapq.heappop(heap)

        res =[[point.x, point.y] for point in heap]
        return res

        