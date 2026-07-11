# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. find the mid pointer
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        rightHalfHead = slow.next
        slow.next = None

        # 2. reverse the right half
        prev = None
        cur = rightHalfHead
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        right_half_reversed_head = prev

        # 3.traverse two linkdelists, at each step, add two elements into new linkedlist
        i = head
        j = right_half_reversed_head
        dummyHead = ListNode()
        cur = dummyHead
        while i and j:
            cur.next = i
            i = i.next
            cur.next.next = j
            j = j.next
            cur = cur.next.next

        if i:
            cur.next = i

        head = dummyHead.next




