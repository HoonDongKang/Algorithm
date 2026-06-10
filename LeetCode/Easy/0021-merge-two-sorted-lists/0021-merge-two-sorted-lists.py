# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        heap = []

        if list1:
            heapq.heappush(heap, (list1.val, 0, list1))
        if list2:
            heapq.heappush(heap, (list2.val, 1, list2))

        while heap:
            val, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next