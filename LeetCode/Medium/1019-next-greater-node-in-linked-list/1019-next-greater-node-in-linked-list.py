# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        arr = []
        stack = []
        idx = 0

        while cur:
            arr.append(cur.val)
            cur = cur.next

        result = [0] * len(arr)

        for i, num in enumerate(arr):
            if stack:
                while stack and arr[stack[-1]] < num:
                    idx = stack.pop()
                    result[idx] = num

            stack.append(i)
        
        return result