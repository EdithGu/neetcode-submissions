# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        # first move fast pointer n steps forward
        fast = head
        while n>0:
            n -= 1
            fast = fast.next

        #print(fast.val)
        # move slow and fast together
        slow = head
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        print(slow.val)
        print(prev.val)
        prev.next = slow.next
        return dummyHead.next
            

