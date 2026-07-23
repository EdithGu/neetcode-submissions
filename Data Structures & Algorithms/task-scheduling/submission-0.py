class Solution:
    class maxHeapItem:
        def __init__(self, task:str, freq:int) :
            self.task = task
            self.freq = freq

        def __lt__(self, other):
            if self.freq > other.freq:
                return True
            else:
                return False

        def __repr__(self):
            return f"{[self.task, self.freq]}"

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count each task's freq
        task_freq = {} #{"A": 3, ...}
        for i in tasks:
            freq = task_freq.get(i, 0) + 1
            task_freq[i] = freq


        # push them all into maxHeap
        maxHeap = []
        for task, freq in task_freq.items():
            heapq.heappush(maxHeap, self.maxHeapItem(task, freq))
        print(maxHeap)

        time = 0

        # bring new available task from queue back to maxHeap
        # pop top, updates its next available time, add it to queue
        queue = collections.deque()
        while maxHeap or queue:
            
            if queue and queue[0][1] == time:
                print(f"/n first ele from current queue:{queue[0]}")
                heapq.heappush(maxHeap, queue.popleft()[0])
            print(f"current maxHeap:{maxHeap}")

            if maxHeap:
                taskItem = heapq.heappop(maxHeap)
                taskItem.freq -= 1
                if taskItem.freq != 0:
                    print(f"{(taskItem, time+1+n)}")
                    queue.append((taskItem, time+1+n))
                    print(f"{queue[0][0], queue[0][1]}")

            time += 1

        return time


        


