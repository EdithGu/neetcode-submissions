class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        # index of non increasing order of their value
        q = collections.deque()

        left = 0
        res = []

        for right in range(len(nums)):
            if right - left + 1 > k:
                if q[0] == left:
                    q.popleft()
                left += 1

            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # put right into deque
            q.append(right)

            if right - left + 1 == k:
                res.append(nums[q[0]])

        return res
