class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        while self.maxHeap and (not self.minHeap or -self.maxHeap[0] >= self.minHeap[0]):
            poppedEle = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, poppedEle)
        if len(self.maxHeap)-len(self.minHeap) >= 2:
            while len(self.maxHeap)-len(self.minHeap) > 1:
                poppedEle = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, poppedEle)
        elif len(self.minHeap)-len(self.maxHeap) >= 2:
            while len(self.minHeap)-len(self.maxHeap) > 1:
                poppedEle = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -poppedEle)

    def findMedian(self) -> float:
        if (len(self.maxHeap)+len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return self.minHeap[0]
        
        