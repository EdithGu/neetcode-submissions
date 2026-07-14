class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0 # fast and slow always represent index

        # there must be a cycle 
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]

            if fast == slow:
                return fast