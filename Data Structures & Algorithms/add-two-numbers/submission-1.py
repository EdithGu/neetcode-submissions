# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry_on = 0
        dummyHead = ListNode()
        cur = dummyHead

        while p1 or p2:
            if not p1:
                total = 0 + p2.val + carry_on
                p2 = p2.next
            elif not p2:
                total = p1.val + 0 + carry_on
                p1 = p1.next
            else:
                total = p1.val + p2.val + carry_on
                p1 = p1.next
                p2 = p2.next
            
            ones_digit = total % 10
            carry_on = total // 10

            cur.next = ListNode(val=ones_digit)
            cur = cur.next

        if carry_on:
            cur.next = ListNode(val = carry_on)

        return dummyHead.next
