# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # edge case
        if len(lists)==0 :
            return None

        # minHeap saves k nodes from each subLists
        minHeap = []
        index = 0
        for sublist_node in lists:
            if sublist_node: 
                # in case the sub-list is None
                heapq.heappush(minHeap,(sublist_node.val, index, sublist_node))
                index += 1

        # each time pop out an ele from minHeap, add it to res linkedlist
        # upadte pointer to its next which is in the sublist that the popped out ele is from
        dummyHead = ListNode()
        cur = dummyHead
        while minHeap:
            popped_out_node = heapq.heappop(minHeap)[2]
            cur.next = popped_out_node
            cur = cur.next
            next_node = popped_out_node.next
            if next_node:
                heapq.heappush(minHeap,(next_node.val, index, next_node))
                index += 1

        return dummyHead.next





