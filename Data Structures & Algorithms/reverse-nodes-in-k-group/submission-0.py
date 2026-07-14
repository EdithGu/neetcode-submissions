# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return None

        dummyHead = ListNode()
        dummyHead.next = head
        start = head
        end = head
        prevTail = dummyHead

        while end:
            count = 1
            while count < k and end.next:
                print(end.val)
                end = end.next
                count += 1

            print(f"count:{count}")
            if count != k:
                prevTail.next = start
                return dummyHead.next

            nextStart = end.next
            print(f"nextStart:{nextStart.val if nextStart is not None else None}")
            newHead = self.reverse(start, end)
            prevTail.next = newHead
            prevTail = start

            start = end = nextStart

        return dummyHead.next

    def reverse(self, start:'ListNode', end:'ListNode') -> 'ListNode':
        end.next = None
        prev = None
        cur = start

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

